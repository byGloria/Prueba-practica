import pytest
from sistema_ventas import Caja, ExcepcionDevolucion, ExcepcionDescuento


class TestRN2Devoluciones:
    """Pruebas para RN-2: El cajero no puede aceptar devoluciones."""

    @pytest.fixture
    def caja(self):
        return Caja()

    def test_ac2_no_se_puede_devolver_producto(self, caja):
        """AC-2: Dado que el cajero no puede aceptar devoluciones, cuando el cliente pide una devolución,
        entonces se rechaza la petición de reingresar al sistema dicho producto."""
        # Dado
        producto = "ProductoA"

        # Cuando y Entonces
        with pytest.raises(ExcepcionDevolucion) as exc_info:
            caja.procesar_devolucion(producto)

        assert "no puede aceptar devoluciones" in str(exc_info.value)
        assert "rechazada" in str(exc_info.value)

    def test_ac2_devolucion_devuelve_false_si_no_hay_producto(self, caja):
        """Si no hay producto, la devolución no se procesa."""
        resultado = caja.procesar_devolucion(None)
        assert resultado is False


class TestRn1UnSoloDescuento:
    """Pruebas para RN-1: un cliente no puede tener más de un descuento aplicado en una compra."""

    @pytest.fixture
    def caja(self):
        return Caja()

    def test_ac1_primer_descuento_se_aplica(self, caja):
        """AC-1: El primer descuento se aplica correctamente."""
        resultado = caja.aplicar_descuento('PROMO10')
        assert resultado is True
        assert caja.descuento == 'PROMO10'

    def test_ac1_segundo_descuento_rechazado(self, caja):
        """AC-1: Si ya hay un descuento, el segundo se rechaza y se conserva el primero."""
        caja.aplicar_descuento('PROMO10')
        with pytest.raises(ExcepcionDescuento) as exc_info:
            caja.aplicar_descuento('EXTRA20')
        assert 'ya tiene un descuento' in str(exc_info.value)
        assert 'PROMO10' in str(exc_info.value)
        assert caja.descuento == 'PROMO10'

    def test_ac1_descuento_original_se_conserva(self, caja):
        """AC-1: Tras rechazar el segundo descuento, el primero sigue vigente."""
        caja.aplicar_descuento('DESCUENTO15')
        with pytest.raises(ExcepcionDescuento):
            caja.aplicar_descuento('DESCUENTO25')
        assert caja.descuento == 'DESCUENTO15'

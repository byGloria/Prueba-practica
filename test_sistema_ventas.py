import pytest
from sistema_ventas import Caja, ExcepcionDevolucion


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

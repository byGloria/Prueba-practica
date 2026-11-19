class ExcepcionDescuento(Exception):
    pass


class Caja:
    def __init__(self):
        self.ventas = []
        self.descuento = None

    def aplicar_descuento(self, codigo):
        if self.descuento is not None:
            raise ExcepcionDescuento(f"No se puede aplicar el descuento {codigo}. El cliente ya tiene un descuento '{self.descuento}' aplicado en esta compra.")
        self.descuento = codigo
        return True

    def registrar_venta(self, producto, cantidad, precio):
        venta = {
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio
        }
        self.ventas.append(venta)
        return venta

    def procesar_devolucion(self, producto):
        if producto:
            raise ExcepcionDevolucion("El cajero no puede aceptar devoluciones. La petición ha sido rechazada.")
        return False

class ExcepcionDevolucion(Exception):
    pass

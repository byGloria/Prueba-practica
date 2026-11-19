class Caja:
    def __init__(self):
        self.ventas = []

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

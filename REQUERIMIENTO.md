Requerimientos del sistema de ventas

RN-1: Un cliente no puede tener mas de un descuento aplicado en una compra.
RN-2: El cajero no puede aceptar devoluciones.

AC-1: 
Dado que se se esta aplicando un descuento en una copra
Cuando se aplica mas de un descuento
Entonces se rechaza la aplicación del segundo.

AC-2:
Dado que el cajero no puede aceptar devoluciones
Cuando el cliente pide una devolucion
Entonces se rechaza la petición de reingresar al sistema dicho producto.

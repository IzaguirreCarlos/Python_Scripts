""""Crea un script que dada una lista con los Productos
Sus Precios y las Unidades vendidas .Imprima la cantidad Total de ventas
El dinero facturado por cada Producto ..Y el Dinero Total"""

""""Tu has vendido 5 de estos Productos .En las siguientes Cantidades

PRODUCTO 1 :  3 unidades
PRODUCTO 2 :  1 unidad
PRODUCTO 5 :  7 unidades
PRODUCTO 6 :  2 unidades
PRODUCTO 9 :  4 unidades
"""

""""precio de cada producto:

Producto  1 : 30.00 $
Producto  2 : 9.O8 $
Producto  3 : 42.O5 $
Producto  4 : 32.06 $
Producto  5 : 71.05 $
Producto  6 : 45.00 $
Producto  7 : 20.00 $
Producto  8 : 55.00 $
Producto  9 : 25.03 $
Producto 10 : 60.00 $
"""

#---lista de productos y precio--
#-- mas lista de unidades vendidas de cada producto

precio_producto = [30.0, 9.8, 42.5, 32.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_producto = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
#facturacion_producto = []

total_ventas = sum(unidades_producto)

#----bucle que recorra los productos (precio mas unidades vendidas)  ------
dinero_total = 0
for i in range(0, len(precio_producto)):
    dinero_por_producto = precio_producto[i] * unidades_producto[i]
    #facturacion_producto.append(dinero_por_producto)
    dinero_total = dinero_total + dinero_por_producto
    print(f"La facturacion por  El producto {i + 1 }  Es : {dinero_por_producto }  USD. ")

#----imprimir resultado ------------
print("El numero Total de unidades vendidas,",total_ventas,"USD.")
#print("La facturacion por producto es :",facturacion_producto)
print("El dinero Total facturado es :",dinero_total,  "USD.")


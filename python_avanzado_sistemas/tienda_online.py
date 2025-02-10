"""
TIENDA ONLINE
Crea una clase "Producto" con atributos como nombre,
precio y numero en stock. Luego, crea una clase
"Tienda" que contenga una lista de productos disponibles
y métodos para agregar productos, mostrar el inventario y realizar una compra."""

class Producto:
    # Constructor de la clase Producto, inicializa nombre, precio y stock
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


class Tienda:
    # Constructor de la clase Tienda, inicializa la lista de productos vacía
    def __init__(self):
        self.productos = []

    # Método para agregar un producto a la lista de productos disponibles
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar el inventario de productos en la tienda
    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"{producto.nombre} - Precio: {producto.precio} EU  - Stock: {producto.stock}")

    # Método para realizar una compra de un producto
    def comprar_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Compra exitosa. Total: {producto.precio * cantidad} EU")
                else:
                    print("No hay suficiente stock.")

                return

        print("Producto no encontrado")

# Ejemplo de Uso
tienda = Tienda()  # Crear una instancia de Tienda
producto1 = Producto("Camiseta", 20, 50)  # Crear un producto "Camiseta"
producto2 = Producto("Pantalon", 30, 30)  # Crear un producto "Pantalon"

tienda.agregar_producto(producto1)  # Agregar producto1 a la tienda
tienda.agregar_producto(producto2)  # Agregar producto2 a la tienda
tienda.mostrar_inventario()  # Mostrar el inventario de productos en la tienda

tienda.comprar_producto("Camiseta", 55)  # Intentar comprar 55 camisetas
tienda.mostrar_inventario()  # Mostrar el inventario después de intentar la compra


        

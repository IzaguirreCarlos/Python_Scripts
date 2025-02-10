"""
SISTEMA DE GESTION DE BIBLIOTECA
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:

1. “Libro”: Representa un libro con atributos como título,
autor y número de ejemplares disponibles.

2. “Usuario”: Representa a un usuario de la biblioteca con atributos como nombre,
número de identificación y lista de libros prestados.

3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar libros,
prestar libros a usuarios, devolver libros y mostrar el inventario.
"""

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro al inventario de la biblioteca.
        :param libro: El objeto Libro a agregar.
        """
        self.libros.append(libro)

    def prestar_libro(self, usuario, titulo):
        """
        Presta un libro a un usuario si está disponible.
        :param usuario: El objeto Usuario que solicita el préstamo.
        :param titulo: El título del libro a prestar.
        """
        for libro in self.libros:
            if libro.titulo == titulo and libro.ejemplares_disponibles > 0:
                usuario.libros_prestados.append(libro)
                libro.ejemplares_disponibles -= 1
                print(f"El libro {titulo} ha sido prestado a {usuario.nombre}")
                return
        print("El ejemplar no está disponible")

    def devolver_libro(self, usuario, titulo):
        """
        Devuelve un libro prestado por un usuario.
        :param usuario: El objeto Usuario que devuelve el libro.
        :param titulo: El título del libro a devolver.
        """
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                usuario.libros_prestados.remove(libro)
                libro.ejemplares_disponibles += 1
                print(f"El libro {titulo} ha sido devuelto por {usuario.nombre}")

    def mostrar_inventario(self):
        """
        Muestra el inventario de libros disponibles en la biblioteca.
        """
        for libro in self.libros:
            print(f"{libro.titulo} de {libro.autor} - Disponibles: {libro.ejemplares_disponibles}")


# Ejemplo de Uso
biblioteca = Biblioteca()  # Crear una instancia de Biblioteca
libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 3)  # Crear un libro
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 5)  # Crear otro libro

biblioteca.agregar_libro(libro1)  # Agregar libro1 al inventario de la biblioteca
biblioteca.agregar_libro(libro2)  # Agregar libro2 al inventario de la biblioteca

biblioteca.mostrar_inventario()  # Mostrar el inventario de la biblioteca

usuario1 = Usuario("Lara", "12345")  # Crear un usuario1
usuario2 = Usuario("Ana", "54321")  # Crear un usuario2

biblioteca.prestar_libro(usuario1, "El Gran Gatsby")  # Prestar libro1 a usuario1
biblioteca.prestar_libro(usuario2, "Cien Años de Soledad")  # Prestar libro2 a usuario2

biblioteca.mostrar_inventario()  # Mostrar el inventario de la biblioteca después de prestar libros

biblioteca.devolver_libro(usuario1, "El Gran Gatsby")  # Devolver libro1 prestado por usuario1

biblioteca.mostrar_inventario()  # Mostrar el inventario de la biblioteca después de devolver un libro
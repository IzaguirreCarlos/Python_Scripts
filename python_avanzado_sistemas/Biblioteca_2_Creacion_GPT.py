class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, id_usuario, titulo):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.titulo == titulo and l.ejemplares > 0), None)
        if usuario and libro:
            usuario.libros_prestados.append(libro)
            libro.ejemplares -= 1

    def devolver_libro(self, id_usuario, titulo):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.titulo == titulo), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                libro.ejemplares += 1

    def mostrar_inventario(self):
        for libro in self.libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Ejemplares: {libro.ejemplares}")

# Ejemplo de uso
biblioteca = Biblioteca()
libro1 = Libro("La Ave Fenix","George Orwell", 5)
libro2= Libro("La Estacion","Carlos Alberto", 1)
usuario1 = Usuario("Juan Pérez", 1)

biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro1)
biblioteca.usuarios.append(usuario1)
biblioteca.mostrar_inventario()

# biblioteca.prestar_libro(0, "La Ave Fenix")
# biblioteca.devolver_libro(0,"La Ave Fenix")
# biblioteca.mostrar_inventario()
# biblioteca.usuarios.append(usuario1)
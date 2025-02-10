"""
Imagina que estás desarrollando un sistema de reservas de vuelos para una aerolínea. 
Crea un sistema de clases que permita a los usuarios realizar reservas de vuelos. 
Aquí tienes una posible estructura:

- Clase base: `Vuelo`
  - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de pasajeros
  - Métodos: agregar pasajero, verificar disponibilidad de asientos

- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
  - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, trabajo)

Resuelve el problema creando instancias de estas clases y realizando 
reservas para diferentes vuelos y tipos de vuelos especiales.
"""

# Definición de la clase base para vuelos
class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        """
        Constructor de la clase Vuelo.
        """
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []  # Lista para almacenar pasajeros

    def verificar_disponibilidad(self):
        """
        Verifica la disponibilidad de asientos en el vuelo.
        Retorna:
            int: Número de asientos disponibles.
        """
        return self.capacidad - len(self.pasajeros)

    def agregar_pasajero(self, pasajero):
        """
        Agrega un pasajero al vuelo, si hay asientos disponibles.
        Parámetros:
            pasajero (str): Nombre del pasajero a agregar.
        """
        if self.verificar_disponibilidad() > 0:
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero} agregado al vuelo {self.numero}")
        else:
            print("No hay asientos disponibles en este vuelo")

# Definición de la clase derivada para vuelos especiales
class VueloEspecial(Vuelo):
    def __init__(self, numero, origen, destino, capacidad, motivo):
        """
        Constructor de la clase VueloEspecial.
        """
        # Llama al constructor de la clase base para inicializar atributos comunes
        super().__init__(numero, origen, destino, capacidad)
        self.motivo = motivo

# Ejemplo de uso de las clases
vuelo_regular = Vuelo("UA30", "NY", "MAD", 150)
vuelo_regular.agregar_pasajero("Juan")
print("Asientos disponibles:", vuelo_regular.verificar_disponibilidad())

vuelo_especial = VueloEspecial("UA31", "MIA", "BAR", 100, "Vacaciones")
vuelo_especial.agregar_pasajero("Laura")
print("Asientos disponibles en el vuelo especial:", vuelo_especial.verificar_disponibilidad())
print("Motivo del vuelo especial:", vuelo_especial.motivo)
"""
Supongamos que estás construyendo un sistema de gestión de empleados para una empresa. 
Crea un sistema de clases que maneje la información de los empleados, incluyendo empleados 
a tiempo completo y empleados a tiempo parcial.

- Clase base: `Empleado`
  - Atributos: nombre, apellido, salario base

- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
  - Atributo adicional: bono anual

- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
  - Atributo adicional: horas trabajadas por semana

Resuelve el problema creando instancias de estas clases y calculando los salarios 
totales para diferentes tipos de empleados.
"""

# Definición de la clase base para todos los empleados
class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base

# Definición de la clase derivada para empleados a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono_anual):
        """
        Llama al constructor de la clase base para inicializar atributos comunes
        """
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario_total(self):
        """
        Calcula el salario total sumando el salario base y el bono anual
        """
        return self.salario_base + self.bono_anual

# Definición de la clase derivada para empleados a tiempo parcial
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, horas_trabajadas):
        " Llama al constructor de la clase base para inicializar atributos comunes"
        super().__init__(nombre, apellido, salario_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_total(self):
        """ 
        Calcula el salario total multiplicando el salario base por las horas trabajadas en un mes
        Se asume que la jornada es semanal y se multiplica por las semanas y meses en un año
        """
        return 12 * 4 * self.salario_base * self.horas_trabajadas

# Ejemplo de uso de las clases
empleado_tiempo_completo = EmpleadoTiempoCompleto("Juan", "Rodriguez", 50000, 3000)
print("Salario total del empleado a tiempo completo:", empleado_tiempo_completo.calcular_salario_total())

empleado_tiempo_parcial = EmpleadoTiempoParcial("Ana", "Martinez", 30, 25)
print("Salario total del empleado a tiempo parcial:", empleado_tiempo_parcial.calcular_salario_total())

# Ejercicio 11: Ejercicio de Memoización en Costos de Envío

# Imagina que estás trabajando en un sistema de gestión de costos de envío para una empresa de logística. El sistema debe calcular el costo de envío para diferentes destinos, distancias y pesos de paquetes. Implementa una función llamada calcular_costo_envio que tome como entrada un destino, una distancia en kilómetros y un peso en kilogramos, y devuelva el costo total del envío.

# Requerimientos:
# El costo base de envío es de 5.0.
# El costo por kilómetro de distancia es de 0.1.
# El costo por kilogramo de peso es de 0.2.
# Implementa la función de manera eficiente utilizando memoización para evitar recalcular el costo para los mismos destinos, distancias y

import functools
import time

@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino,distancia,peso):
  costo_base=5
  costo_distancia=distancia *0.1
  costo_peso=peso*0.2
  #Calculamos el costo total
  costo_total = costo_base+costo_distancia+costo_peso
  return costo_total

#Ejemplo de uso
#/////////////////Sin memoizacion
inicio=time.time()
destino_1 = "Ciudad A"
distancia_1 = 150
peso_1 = 2.5
costo_sin_memo_1=calcular_costo_envio(destino_1,distancia_1,peso_1)
destino_2 = "Ciudad B"
distancia_2 = 100
peso_2 = 4.5
costo_sin_memo_2=calcular_costo_envio(destino_2,distancia_2,peso_2)
final=time.time()

#/////////////////Con memoizacion
inicio_2=time.time()
destino_1 = "Ciudad A"
distancia_1 = 150
peso_1 = 2.5
costo_con_memo_1=calcular_costo_envio(destino_1,distancia_1,peso_1)
destino_2 = "Ciudad B"
distancia_2 = 100
peso_2 = 4.5
costo_con_memo_2=calcular_costo_envio(destino_2,distancia_2,peso_2)
final_2=time.time()

print("Costo sin memo para Ciudad A es de: ",costo_sin_memo_1)
print("Costo sin memo para Ciudad B es de: ",costo_sin_memo_2)
print("Costo sin memo para Ciudad A es de: ",costo_con_memo_1)
print("Costo sin memo para Ciudad B es de: ",costo_con_memo_2)

print("Tiempo sin memoizacion es de: ",(final-inicio))
print("Tiempo con memoizacion es de: ",(final_2-inicio_2))
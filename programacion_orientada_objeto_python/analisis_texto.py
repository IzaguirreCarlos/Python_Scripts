# Ejercicio 12: Ejercicio de Memoización en Análisis de Texto

# Imagina que estás trabajando en un sistema de análisis de texto que requiere calcular la frecuencia de ocurrencia de palabras en un conjunto de documentos. Implementa una función llamada calcular_frecuencia_palabras que tome como entrada un texto y devuelva un diccionario que muestre la frecuencia de cada palabra en el texto.

# La función debe ser capaz de manejar textos y ser insensible a mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la misma palabra).
# Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que no aportan información relevante al análisis.
# Utiliza memoización para evitar recalcular la frecuencia de palabras para el mismo texto.

import functools
import re
import time
@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras(texto):
  #Preprocesamiento del texto
  texto=texto.lower()
  texto=re.sub(r'[^a-z\s]', '', texto) #Eliminar puntacion o caracteres no deseados
  palabras=texto.split()

  #Excluir palabras comunes
  palabras_comunes = set(["el", "la", "los", "las", "de", "en", "y", "a", "con", "es", "un", "una", "para"])

  palabras=[palabra for palabra in palabras if palabra not in palabras_comunes]

  #Conteo de frecuencia
  frecuencia={}
  for palabra in palabras:
    frecuencia[palabra]=frecuencia.get(palabra,0)+1
  return frecuencia

# Ejemplo de uso
texto_1 = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
adarga antigua, rocín flaco y galgo corredor.
Una olla de algo más vaca que carnero, salpicón las más noches,
duelos y quebrantos los sábados, lentejas los viernes,
algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.
El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo,
los días de entre semana se honraba con su vellorí de lo más fino.
Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte,
y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera.
Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes,
enjuto de rostro, gran madrugador y amigo de la caza.
Quieren decir que tenía el sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia en los autores que deste caso escriben),
aunque por conjeturas verosímiles se deja entender que se llama Quijana;
pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.
"""

texto_2 = "Otro ejemplo de Análisis de texto con palabras repetidas. Ejemplo y texto se repiten."

inicio_1=time.time()
frecuencia_sin_memo_1=calcular_frecuencia_palabras(texto_1)
frecuencia_sin_memo_2=calcular_frecuencia_palabras(texto_2)
final_1=time.time()
inicio_2=time.time()
frecuencia_con_memo_1=calcular_frecuencia_palabras(texto_1)
frecuencia_con_memo_2=calcular_frecuencia_palabras(texto_2)
final_2=time.time()

print("Frecuencia de palabras para texto_1 sin memoizacion: ",frecuencia_sin_memo_1)
print("Frecuencia de palabras para texto_2 sin memoizacion: ",frecuencia_sin_memo_2)
print("Frecuencia de palabras para texto_1 con memoizacion: ",frecuencia_con_memo_1)
print("Frecuencia de palabras para texto_2 con memoizacion: ",frecuencia_con_memo_2)

print("Tiempo sin memoizacion: ",(final_1-inicio_1))
print("Tiempo con memoizacion: ",(final_2-inicio_2))
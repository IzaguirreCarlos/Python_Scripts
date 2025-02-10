""""supongamos una lista e caracteres  llamada "palabra" 
que presente una mano de Juego
.cada string contiene 2 caracteres: el primer caracter es una letra 
de una ficha y el 
segundo el numero que presenta los puntos de la ficha  por ejemplo:
  "A5" representa la ficha con la letra A ,
y un valor de 5 PUNTOS . crea un script que calcule el valor total de los puntos
 en una mano de JUEGO
El valor total sera la suma de los puntos de todas las fichas  de la mano."""

#--lista con las fichas del juego--
juego_de_mano = ["A5", "B3", "C4", "H8", "D10"]

#--bucle en el que recorremos las fichas y sumamos los puntos
#--inicializamos las viriable punto en 0--
puntos = 0
#--recorremos la lista de las fichas del juego de mano--
for ficha in juego_de_mano:
    # sumamos los puntos de cada una de las fichas
    puntos = puntos + int(ficha[1:])

#--imprimir el numero total  de puntos--
print("El numeron toTal de puntos de tu MANO es :",puntos)


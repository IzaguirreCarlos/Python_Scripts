""""CREA UN SCRIP QUE PIDA AL USUARIO UNA PALABRA
Y LUEGO QUE LAS MUESTRE UNA A UNA POR PANTALLA
DE LAS PALABRAS INTRODUCIDAS DE ATRAS PARA ADELANTE"""

#---pedir al usuario una palabra--
palabra = input("Ingrese una palabra ---->>>")
longitud = len(palabra)

#-----bucle que recorra el str palabra por palabra----
for i in range(longitud - 1, -1, -1):
    # que imprima palabra por palabra
    print(palabra[i])

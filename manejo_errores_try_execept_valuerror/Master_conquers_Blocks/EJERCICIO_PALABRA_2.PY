""""CREA UN SCRIP QUE PIDA AL USUARIO UNA PALABRA
Y LUEGO QUE LAS MUESTRE UNA A UNA POR PANTALLA
DE LAS PALABRAS INTRODUCIDAS DE ATRAS PARA ADELANTE"""

#---pedir al usuario una palabra--
palabra = input("Ingrese una palabra ---->>>")

for letra in palabra [::-1]:
    print(letra)
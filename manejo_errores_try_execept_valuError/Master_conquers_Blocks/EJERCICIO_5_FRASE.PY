""""crea un programa en el que se le pregunte al usuario
una frase y una letra .y que cuente el numero de veces que
aparese esa letra , en la frase introducida"""

#  pedir frase. y letra
frase = input("Ingrese una frase:")
letra = input("Ingrese una letra:")

## bucle que recorra la frase 
contador = 0

for caracter in frase:
    if caracter == letra:
        # contador = contador ,,mas 1
                contador += 1


# mostrar el resultado al usuario--- 
print(f"La letra aparese {contador} veces en la Frase")

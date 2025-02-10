""""define una lista de 5 palabras  aleatorias
y una lista de 5 palabras prohibidas que contengan
tres letras. filtra las palabras en tu lista original
y crea una nueva lista de palabras filtradas que
solo contengan aquellas palabras que no tienen ninguna letra prohibida."""

#--crea una lista de palabras aleatorias. y otras de letras prohibidas
##-- y una lista de palabras filtradas--
palabras_alatorias = ["casa", "perro", "gato", "libro", "raton"]
letras_prohibidas =  ["a", "u",]

# inicializar una lista vacia
# donde  anadiremos las palabras filtradas
lista_filtrada = []

# ---bucle para recorrer las lista de palabra--
for palabra in palabras_alatorias:
    #en principiuo incluiremos la palabra a no ser que
    #se compruebe que  contiene una letra prohibida
    incluir = True
    #--bucle para comprobar si los objetos tiene alguna letra prohibida.
    for letra_prohibida in letras_prohibidas:
        ## Si tiene letra prohibida ,no la incluimos en la lista filtrada
        if letra_prohibida in palabra:
            incluir = False

    # comprobamos si debemos incluir la palabra , En caso de 
    # que no tenga letras prohibidas (incluir = true) la incluimos
    if incluir:
        lista_filtrada.append(palabra)

# -----Imprimimos por pantalla las tres listas ------
print("Lista Original :",palabras_alatorias,)
print("Letras Prohibidas:",letras_prohibidas,)
print("Lista Filtrada:",lista_filtrada,)
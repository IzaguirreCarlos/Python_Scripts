""""Escribe un programa en python . Para encontrar los elementos duplicados 
de una lista, anadirlos a una lista y borrarlos de la lista.Despues imprime una
lista con tan solo los elementos unicos"""

lista = [1,2,3,4,5,6,3,7,8,9,8,10]
print("Lista original:",lista)
elementos_duplicados = []
elementos_unicos = []
for elementos in lista:
    if lista.count(elementos) > 1:
        if elementos not in elementos_duplicados:
         elementos_duplicados.append(elementos)
    else:
       elementos_unicos.append(elementos)
print("Elementos unicos:",elementos_unicos)
print("Elementos duplicados:",elementos_duplicados)

       

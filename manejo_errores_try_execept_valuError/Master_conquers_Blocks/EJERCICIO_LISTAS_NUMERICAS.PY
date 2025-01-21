# crea una lista del 1 hasta 100
#numero = list(range(1,101))
#print(numero)

# lista pares , y tambien invertidos
numero = list(range(1,11))
pares = []
for numero in numero:
    if numero % 2 == 0:
        pares.append(numero) 
pares_invertidos = pares[::-1]

print(pares)
print(pares_invertidos)
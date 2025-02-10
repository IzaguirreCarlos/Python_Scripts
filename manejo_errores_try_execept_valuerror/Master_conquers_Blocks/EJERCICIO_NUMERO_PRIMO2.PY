""""dado una lista de numeros enteros ,
has un script en python que  devuelva una lista
con los numeros primos de la lista original
ademas , el script debe devolver  el numero total 
de numeros primos encontrados y la 
suma de los numeros primos encontrados"""

#--lista de numeros enteros
# lista vacia para los numeros primos
# numero total de numeros primos
# suma de los numeros primos encontrados

numeros = [2,3,4,5,6,7,8,9,10]
primos = []
total_primos = 0
suma_primos = 0

# bucle para recorrer la lista de numeros
for numero in numeros:
    # comenzamos suponiendo que los numeros son primos
    primo = True
    #comprobamos si el numero es primo
    for i in range(2, numero):
        # si el numero es divisible por otro
        # numero diferente a este o a 1 entonces
        # no es primo ---- primo = false
        if numero % i == 0:
            primo = False

# si es primo lo anadimos a la nueva lista
if primo == True:
    #  anadimos al nuevo
    primos.append(numero)
    # aumentamos en uno el contador de numeros primos
    total_primos = total_primos + 1
    #sumamos este numero al total de la suma de numeros primos
    suma_primos = suma_primos + numero

# ---Imprimimos los Datos por Pantalla al Usuario---------
print("Numeros Primos:",primos)
print("Total de Numeros Primos:",total_primos)
print("Suma de Numeros Primos:",suma_primos)
print("Total de Numeros Primos:", len(primos))
print("Suma de Numeros Primos:", sum(primos))
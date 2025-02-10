"""" crea un programa que imprima todos los numeros primos del 2 hasta el 100. 
un numero primo es un numero positivo y entero    que no sea 1 o si mismo """

# bucle que recorra los numeros del 2 hasta el 100---
for numero in range(2,101):
    primo = True
    # para dicho numero ahi algun dicho numeron que sea divisor
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero)

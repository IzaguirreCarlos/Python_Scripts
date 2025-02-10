"""" crea un programa que imprima todos los numeros primos del 2 hasta el 100. 
un numero primo es un numero positivo y entero    que no sea 1 o si mismo """

for numero in range(2,101):
    primo = True
    i = 2
    while primo == True and i < numero:
        if numero % i == 0:
            primo = False
            i += 1
    if primo:
        print(numero)
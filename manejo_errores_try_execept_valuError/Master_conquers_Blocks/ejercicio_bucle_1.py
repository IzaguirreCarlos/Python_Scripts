#---escriba un programa que pida al usuario un numero entero. Y muestre por pantalla una estructura  como la de mas abajo,
#--donde el valor de entrada es  el numero de  estrellas en el ...Centro de la estructura----

#--pedir al usuario un numero entero---
num = int(input("introdusca la anchura central (numero entero):"))
#--bucle ascendente---
for i in range(1, num + 1 ):
    print("*" * i + " " * (num - i))
 #---bucle descendente----
 
 
for i in range(num-1,0,-1):
     print("*" * i + " " * (num - i))

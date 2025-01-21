#---escribe un programe que almacene una cadena de caracteres --
#--conrasena en una variable , pregunte al usuario por la contrasena--
##-- hasta que introdusca la contrasena correcta--


#--- pedirle al usuario que ingrese la contrasena--
usuario = str(input("Ingrese la contraseña correcta   --->"))
#--paso 2:  guardar la contrasena en una variable--
contrasena_correcta = ("carlos123")
#----paso 3 : crear un bucle  que pida la contasena al usuario y que a su m
#mismo tiempo pueda salir de EL---
while   usuario == contrasena_correcta:
    print("Acceso Permitido.  ! Su contraseña es correcta !")
    break
else:
    print("Permiso Bloqueado, ! Contraseña Incorrecta " ":(")

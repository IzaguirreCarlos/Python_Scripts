""""supongamos que eres un acministrador de sistemas y que necesitas validar
el acceso a un usuarios a un sitio Web..crea un script que verifique ,
si el Nombre de usuario y contrasena son VALIDOS .Si lo
son Permite el Acceso si los Dos son VALIDOS..."""

# lista de nombres  de usuarios .Y contrasena
nombres_usuarios = ["juan123","ana456","pedro750"]
passwords = ["clave123","clave456","clave750"]
# pedir al usuario su nombre y contrasena
usuario = input("Ingrese su nombre de usuario____")
password = input("Ingrese su contrasena""_____")
# booleano que sera true si el usuarioid
# y contrasena son correctos con los que estan en nuestra lista
credenciales = False
# recorrer la lista de usuarios y contrasenas
for i in range(len(nombres_usuarios)):
    # comprobamos si son iguales a los introducidos por el usuarioç
    if nombres_usuarios[i] == usuario and passwords[i] == password:
    # como son un nombre y contrasena validos 
    # credenciales pasa a ser true
     credenciales = True
# si el usuarioy contrasena son validos Damos la Bienvenida
if credenciales == True:
    print(" Accseso Permitido")
# Si no son Validos denegamos el Acseso
else:
    print("Nombre de Usuario Ho Contrasena Incorrectos")
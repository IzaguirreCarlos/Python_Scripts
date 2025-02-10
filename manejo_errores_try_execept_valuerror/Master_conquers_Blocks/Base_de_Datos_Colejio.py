""""Trabajas en el colegio y estas encargado de 
Mantener un seguimiento de las Notas de los Estudiantes de una clase.
En tu BASE DE DATOS tienes una Lista con los nombres de los Estudiantes,
y para cada Estudiante debes Guardar sus NOTAS provenientes
de deberes , examenes y Proyectos.

Tambien necesitas calcular a notas media de cada
 Estudiantes y la NOTA MEDIA de la clase al Completo.
 
PISTA---Para resolver este problema puedes usar una Lista anidada
Donde Guardemos las notas para cada Estudiantes .Entonces puedes usar
un bucle para recorrer la lista de listas .Y calcular la nota media de
cada Estudiante . Tambien puedes usar otro bucle  para calcular
la NOTA MEDIA de toda la CLASE"""

#---SOLUCION USANDO BUCLES PARA LA MEDIA INDIVIDUAL Y ------
#----LA MEDIA  DE LA CLASE ----
 
# LISTA con los nombres de los alumnos
estudiantes = ["juan","maria","pedro"]

#creamos nuestra base de datos  con las notas
database = []

# pido los datos de las notas para cada estuduiantes
while True:
  try:
     if estudiantes in estudiantes:
    # crear mi lista de notas pidiendo las notas al estudiante
      notas = []
     print(f"ingrese las notas de {estudiantes}")
    #pido la nota de deveres 
     deveres = float(input("ingrese nota de deveres:"))
    # la anado a la lista de notas
     notas.append(deveres)
    #pido la nota de examenes
     examenes = float(input("ingrese nota de examenes:"))
     # la anado a examenes
     notas.append(examenes)
    # pido la nota proyectos
     proyectos = float(input("ingrese nota de deveres:"))
    # la anada a lista proyecto
     notas.append(proyectos)
    #anadir a lka database el nombre y la lista de notas del alumno
     database.append([estudiantes ,notas])
  

print(" ")
print(" ")
print("calculando media individuales y totales ..... ")
print(" ")
print(" ")

# calcular la nota media de cada estudiante
suma_media = 0
for data in database:
  # extraemos el nombre de cada estudiante
  nombre = data[0]
  #extraemos la lista de cada nota del estudiante
  notas = data[1]
  # calculamosn la media del estudiante
  media = sum(notas) / len(notas)
  #imprimimos por pantalla la media den cada estudiante
  input(f"La media de {nombre} es {media :.2f}")
  # calculamos la suma de todas las mnedias
  suma_media = suma_media + media

# dividimos la suma de todas las medias por el numero del alumno
# para obtener la media de toda la clase
media_clase = suma_media / len(database)
# imprimos la media de toda la clase
print(f"La media de la clase Es {:.2f}".format(media_clase))
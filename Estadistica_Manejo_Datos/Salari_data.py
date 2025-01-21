import _csv
import pandas as pd
# DATOS PARA EL ARCHIVO
data = [
    ["Position", "Salario", "Years_of_Experience"],
    ["Software Engineer", 120,000, 5],
    ["Data Analyst", 80,000  ,3],
    ["Manager",       65,000, 7],
    ["DeVoop Senor",   55,000, 2],
]

# CREAR EL ARCHIVO CSV
with open("Salari_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = _csv.writer(file)
    writer.writerows(data)

print("Archivo 'Salari_data.cvs'Creado con Exito.")


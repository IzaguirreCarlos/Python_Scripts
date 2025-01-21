""""Vamos hacer un programa para calcular ahorro anuales del usuario
1) preguntamos cuanto gana la hora
2) preguntamos la cantidad de horas trabajadas en la semana
3) preguntamos cuantos gastos tiene a la semana
4) imprimos el Resultado final por pantalla."""
# --preguntamos precio hora --horas trabajadas---
precio_hora = float(input("Ingrese cuanto Gana por Hora ---->"))
horas_trabajadas = int(input("Ingrese La Cantidad de  Horas Trabajadas ---->"))
#-- ahora preguntamos gastos semanales --
gastos_semanal = float(input("Ingrese sus Gastos Semanales --->"))
# --hacer calculo de Ganancias semanal --
ganancia_semanal = horas_trabajadas * precio_hora
# --hacer calculo de Ganancias anual por Ganancias semanales----
ganancia_anual = ganancia_semanal * 52
#---ahcemos calculo de gastos anuales---
ahorro_anual = ganancia_anual - gastos_semanal * 52
print("Tu Ganancia  Anual es De :,",ganancia_anual,"DOLLARES")
#---imprimir al usuario el Resultado de sus Ganancias anuales por Pantalla--
print("Tu Ahorro Anual es De :,",ahorro_anual,"DOLLARES")
 

 
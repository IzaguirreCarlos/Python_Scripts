#--pedir pago por hora al usuario---
pago_hora = int(input("¿ganancia por hora""----"))
#---horas trabajadas--
hora_trajada = float(input("¿horas trabajas ""-----"))
# ---hacer calculo de semana --
salario_semanal = pago_hora * hora_trajada
# -- hacer calculo ingreso al anual----
salario_anual = salario_semanal * 52
print("--------------------------------------------------------")
#--imprimir al usuario el resultado de ganancias anuales--
(print("su ingreso anual es ---",salario_anual,))
print("--------------------------------------------------------")
#---preguntar al usuario sus gastos semanales-- 
gastos_semanal = float(input("ingrese sus gastos semanales ---=",))
# ---hacer calculo de gastos semanales y anual---
gastos_anual = gastos_semanal * 52
#---calcular ahorro --
ahorro_anual = salario_anual - gastos_anual
print("-----------------------------------------------------------")
# ---------------imprimir el ahorro anual al usuario po PANTALLA - -------------
print("Tu ahorro anual es ---=",ahorro_anual,)

# lista  con las ventas por mes
ventas = [20, 40, 50, 500, 300, 190, 95, 111, 322, 555, 666, 890,]
# lista con las venta por semana
dia_semana = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
# lista donde guardamos las venta por diia
total_ventas = [0, 0, 0, 0, 0, 0, 0]
# recorrer la lista con un bucle
dia_venta = 0
for venta in ventas:
    #  sumar para cada dia de la semana las venta realida
     total_ventas[dia_venta] = total_ventas[dia_venta] + venta
    #  pasamos al dia suiguiente
     dia_venta = dia_venta  + 1
    #  si llegamos al domingo pasamos al lunes
     if dia_venta == 7:
    #    cambiamos el valor al indice aln lunes
       dia_venta = 0
## imprimimos por pantalla las ventas por cada dia de la semana realizadas
# a lo largo de ese mes
for i in range(len(dia_semana)):
    print(dia_semana[i] + ":", total_ventas[i])
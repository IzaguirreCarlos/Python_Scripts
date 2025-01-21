def max_suma_subarreglo(num):
    max_suma = num[0]
    suma_actual = num[0]

    for nu in num[1:]:
        suma_actual = max(nu, suma_actual + nu)
        max_suma = max(max_suma, suma_actual)

        return max_suma
    
num = [-2, 1, -3, 4,  -1, 2, 1, -5, 4]
print(max_suma_subarreglo(num))
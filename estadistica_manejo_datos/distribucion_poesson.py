import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
# SIMULACION DE PROCESO DE DROPOUT

# Parametros
num_neuronas = 100
lambda_poisson = 0.5
num_iteraciones = 1000

# Funciones para simular el dropout . usando distribuciones de Poisson
def simular_dropout(num_neuronas, lambda_poisson):
    return poisson.rvs(mu=lambda_poisson, size=num_neuronas)
    # esta funcion se llama para cada una de las 100 neuronas

# Simular el dropout en 1000 iteraciones
neuronas_off_cuenta = []

for _ in range(num_iteraciones):
    dropout_mask = simular_dropout(num_neuronas, lambda_poisson)
    num_neuronas = np.sum(dropout_mask)
    neuronas_off_cuenta.append(num_neuronas)

# 2. Calcular y mostrar el numero medio de neuronas Desactivadas
mean_neuronas_off = np.mean(neuronas_off_cuenta)
print(f"Numero Medio de Neuronas Desactivdas en {num_iteraciones}  iteraciones: {mean_neuronas_off:.2f}")

# Mostrar Graficas de la Distrubucion de Neuronas Desactivadas
plt.hist(neuronas_off_cuenta, bins=30, density=True, alpha=0.6, color="g", edgecolor="black")
plt.title("Distribucion de Neuronas Desactivadas en 1000 iteraciones")
plt.xlabel("Numeros de Neuronas Desactivadas")
plt.ylabel("Frecuencia")
plt.show()
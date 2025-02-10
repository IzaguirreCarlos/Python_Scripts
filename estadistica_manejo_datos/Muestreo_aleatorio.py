import numpy as np
# GENERAMOS UNA POBLACION DE EJEMPLO
poblacion=np.arange(1, 101)

tamano_muestra_1 =10

# SELECCIONAMOS LAS MUESTRA USANDO UN MUESTRO SIMPLE
muestra_alatoria_simple =np.random.choice(poblacion,tamano_muestra_1,replace=False)
print("Muestra alatoria Simple:",muestra_alatoria_simple) 
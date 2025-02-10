import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr, spearmanr

# DATOS DE EJEMPLO
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # variable ind
y = np.array([2, 3, 5, 7, 11])  # variables dependiente

# ajustar el modelo

model =LinearRegression()

model.fit(x,y)

y_pred=model.predict(x)

a=model.intercept_
b=model.coef_[0]

print(f"Interseccion (a):{a}")
print(f"Pendiente (b):{b}")

# CALCULO DE CORRELACION DE PEARSON
correlacion_pearson, _=pearsonr(x.flatten(),y)

# CALCULAR EL COEFICOINTE DE SPEARMAN
correlacion_spearman=spearmanr(x.flatten(),y)

print(f"coeficiente de correlacion de pearson:{correlacion_pearson}")
print(f"coeficiente de correlacion de spearman:{correlacion_spearman}")

# CREAR UNA GRAFICAS DE LOS EJEMPLOS ANTERIORES`
plt.scatter(x,y,color="blue") # datos originales
plt.plot(x,y_pred,color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("regresion Lineal")
plt.show()

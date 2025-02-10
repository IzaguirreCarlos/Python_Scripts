import scipy.stats as stats

# PARAMETROS DE LA DISTRIBUCION NORMAL
mu = 170 # MEDIA
sigma = 12 # DESVIACION ESTANDAR

# DEFINIR LOS LIMITIS DEL INTERVALO
x1 = 189 # Limiti Inferior del Intervalo
x2 = 190 # Limiti Superior del Intervalo

# CALCULAR LA PROBABILIDAD  P(x1 < x < x2) donde x - N(mu, sigma)
## USAMOS LA FUNCION DE DISTRIBUCION ACUMULATIVA (CDF) DE LA DISTRIBUCION NORMAL
prob = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)

### MOSTRAR EL RESULTADO
print(f"La Probabilidad de que un Alumno Mida entre:  {x1} CM y : {x2} CM es Aproximadamente : {prob*100:.4f} %")





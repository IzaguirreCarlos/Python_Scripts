import numpy as np
import pandas as pd
data={
    "individuos":np.arange(1,101),
    "estrato": np.repeat(["A","B","C","D"],25)
}

poblacion=pd.DataFrame(data)
Tamano_muestra=12

# Muestreo Estratificado
muestra_estratificada=poblacion.groupby("estrato",group_keys=False).apply(lambda x: x.sample(int(np.rint(Tamano_muestra * len(x) / len(poblacion)))))

print("Muestra Estratificada \n",muestra_estratificada)
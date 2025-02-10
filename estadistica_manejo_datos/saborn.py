import seaborn as sns
import matplotlib.pyplot  as plt 

datas = sns.load_dataset("iris")

#print(data)

# GRAFICO DE DISPERSION
sns.scatterplot(data=datas,x="sepal_length" ,y="sepal_width")
plt.title("Graficos de Dispercion de Longitud del sepalo vs Ancho Carlos")
plt.xlabel="sepal_length"
plt.ylabel="sepal_width"
plt.show()

# GRAFICO DE BARRA
sns.barplot(data=datas, x="species",y="sepal_length")
plt.title("Graficos de Barra del sepalo por species CARLOS_2")
plt.xlabel="species"
plt.ylabel="sepal_length"
plt.show()

# GRAFICOS DE HISTOGRAMA
sns.histplot(datas["sepal_length"],bins=10)
plt.title("Grafico de Historiograma CARLOS_3")
plt.xlabel="longitud del sepalo"
plt.ylabel="numero de repeticion"
plt.show()

# GRAFICO DE VIOLIN
sns.violinplot(data=datas,x="species" ,y="sepal_length")
plt.title="GRAFICO DE VIOLIN CARLOS_4"
plt.show()

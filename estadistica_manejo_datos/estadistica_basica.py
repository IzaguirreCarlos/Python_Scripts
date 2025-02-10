
import pandas as pd
import numpy as np

# CALCULAR MEDIA FORMA FACIL
def calculo(vector):
    # media
    suma =0
    n=0 
    suma =sum(vector)
    n=len(vector)
    media=(1/n)*suma
    print(f"media_2  {media:.2f}")
vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]
#calculo(vector)

df=pd.read_csv("Salary_data.py",sep=";")

print(df.head())

# Load Balance Sheet data (T0)
#df= pd.read_csv('position_salary.csv')

#print(df.head())


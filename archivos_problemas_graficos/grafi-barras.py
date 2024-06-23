import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

total_ingreso = df["ingresos"].sum()

#total de ingreso
print(total_ingreso)

#mostrando el grafico
plt.show() 





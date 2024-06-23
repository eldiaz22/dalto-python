import pandas as pd

df = pd.read_csv("archivo\\datos.csv") # names =["names", "lastname", "age"]
df2 = pd.read_csv("archivo\\datos.csv") # names =["names", "lastname", "age"]


#nombres = df["names"]

#ordenar datos
valor = df.sort_values("edad", ascending=False)
print(valor)



#concatenar 
unir = pd.concat([df,df2])
print(unir)

print("-------------------HEAD---------------------------")
#accediendo a la primeras 3 filas con head()
primeras_filas = df.head(1)
print(primeras_filas)

print("-------------------TAIL---------------------------")

#accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(1)
print(ultimas_filas)



                            #accediendo a la cantidad de filas y columnas con 
print("-------------------ver la cantidad de fila y columna---------------------------")
#filasycolumna = df.shape
#filasTotales = filasYcolumna[0]
filas_totales,columnas_totales = df.shape
print(filas_totales)


                                #obteniendo data estadística del dataframe:
df_info = df.describe()
print(df_info)



                                ##accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]
print(apellidos_loc)

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]


#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:] #dataframe.iloc[filas, columnas]
print(fila_3)

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]
print(fila_3)


#accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df["edad"]>30,:"nombre"]
print(mayor_que_30)
#cadena = "0123456789"
#print(cadena[0:9])
#Promedio de duraciòn
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duraciòn

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacìo removido
tiempo_vacio_promedio =  100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto =  100 - dalto_curso * 1000 // crudo_dalto / 10


#Mostrando las diferencias de duraciòn (ejercicio A)

print("----------------")
print("El curso de dalto dura:")
print(f' - un {diferencia_con_min}% menos que el màs rapido')
print(f' - un {diferencia_con_max}% menos que el màs lento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print("----------------")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso eliminò el {tiempo_vacio_dalto}% de tiempo vacio')
print("----------------")

#Mostrando diferencias si los cursos duraran 10 horas (ejercicio C)
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso')
print("----------------")






#le pedimos al usuario que nos diga una frase (o varias)
frase = input("Decime una frase y te calculo cuanto tardarìas si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)



#en caso de que tarde màs de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedì un testamento")
    
#Calculamos cuanto tardaría en decir las palabras y se lo decimos    
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarìas {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo dirìa en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos')

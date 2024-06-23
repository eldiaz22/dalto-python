#creando una lista (se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"] #arrays
        #elemento 1 pero indice 0     
print(lista[0])


#creando una tupla (no pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto")
#esto es vàlido
#lista[3] = "Maquinola"
#esto no
#tupla[3] = "Maquinola"

#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"}


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Lucas Dalto", #0
    'canal' : "Soy Dalto", #1
    'esta_emocionado' : True, #2
    'altura' : 1.85, #3
    'dato_duplicado' : "Soy Dalto" #4
}

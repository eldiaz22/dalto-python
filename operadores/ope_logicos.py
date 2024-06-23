#AND SI AMBAS SE CUMPLEN DEVUELVEN TRUE
# y si ademas 

Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso

# if edad > 17 & dinero == 100:
#     print("usted puede entrar al concierto")
    
# else: print("usted no puede entrar al concierto ")


#OR FALSO SI NINGUNA SE CUMPLE
#y si no

Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT

Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True


print("..........................PRACTICA DE OPERADORES LOGICOS.............")

edad = 16
tiene_Boleto = True
tiene_Permiso =  False

if (edad > 17 and tiene_Boleto == True) or (tiene_Permiso == True and tiene_Boleto == True):
    print("Usted va a entrar al concierto.")
else:
    print("Usted no va a entrar.")

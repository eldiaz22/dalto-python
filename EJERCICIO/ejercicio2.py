#creando una funciòn que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse  #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True


def primo_hasta(num):
    lista_primos = []
    for i in  range (2,num+1):
        es_primo(i)
        resultado = es_primo(i)
        if resultado == True: lista_primos.append(i)
    return lista_primos
        

numero = primo_hasta(100)


print(numero)
 
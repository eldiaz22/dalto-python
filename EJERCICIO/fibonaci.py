#creando una funcion que muestre la serie fibonacci entre 0 el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b) # se pone b pq es el numero que cambia
            a,b = b,a+b
            #a,b = 1, 0 + 1               
            #a =1, B = 1  = B:1 , A:1 + B:1 = b 2
            # a= 1 ; b = 2 = b:2 ,  a: 1 + b:2
resultado = fibonacci(34)
print(resultado)



c,b = 2,4
    # 4
c,b = b, c+b #2+ 4
print(c,b)
    
c,b = b, c+b # 4 + 6 


print(c,b)
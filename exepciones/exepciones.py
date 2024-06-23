def suma():
    while True:
        a = input("Ingrese numero 1: ")
        b = input("ingrese numero 2: ")
        try:
            resultado = int(a) + int(b)
            
        except Exception as e: 
            print(f"te pedi un numero ")
            print(f"ERROR DE {e}")
        else: 
            break
        finally: print("Esto se ejecuta siempre")
    return resultado

print(suma())
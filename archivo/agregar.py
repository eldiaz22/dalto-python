with open("archivo\\soy_el_mejor.txt", "a", encoding="UTF-8") as archivo:
    for i in range(10):
        archivo.write(f"LINEA {i+1}\n")
    #archivo.writelines([f"LINEA {i+1}\n" for i in range(10)])

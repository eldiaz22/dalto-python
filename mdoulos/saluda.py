import saludaFunction as  saluda  #as hola
from saludaFunction import saludar, saludar_raro
#las funciones se trabajan con s mayuscula
salu = saluda.saludar("Junior")
print(salu)

#from carpeta.modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu


#para ver las propiedades y metodos de el namespace
#print(dir(saluda))


#accedemos al nombre de este modulo
print(__name__)


#accedemos al nombre de este modulo
print(saluda.__name__)

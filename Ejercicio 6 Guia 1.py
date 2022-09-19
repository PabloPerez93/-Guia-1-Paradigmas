#Área de un triángulo. Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base,
#pero sabiendo que su altura es igual al cuadrado de la base.
#Area = (base.altura)/2

#Inicializando variables
altura = 0
base = 0
area = 0

#Cuerpo del programa

base = int(input("Indique la base del triaguno: "))
altura = base ** 2
area = (base * altura)/2

print("La altura del triagulo es de:",altura)
print("El area del triagulo es de :",area,"cms2")

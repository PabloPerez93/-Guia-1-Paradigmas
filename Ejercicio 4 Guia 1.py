#División con resto:
#Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división.

#Inicializacion variables
a = 0
b = 0
resultado = 0
resto = 0

#Cuerpo del programa

a = int(input("a: "))
b = int(input("b: "))

resultado = a/b
resto = a%b

print(f'El resultado de la division es: {(resultado):.2f}')
print(f'El resto de la division es:" {resto:.2f}')
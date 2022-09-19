"""Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo"""

#Inicializacion de variables

n1 = 0
n2 = 0
n3 = 0
resul = 0
#Cuerpo del programa

n1 = int(input("Escriba el primer numero: "))
n2 = int(input("Escriba el segundo numero: "))
n3 = int(input("Escriba el tercer numero: "))
resul = n1 + n2 + n3
print(resul)

if resul > 10:
    print(f'{resul/2:.0f}')

else:
    print(f'{resul**3}')
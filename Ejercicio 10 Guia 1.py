"""Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto."""

#Inicializar Varibales

n1 = 0
n2 = 0

#Cuerpo del programa

n1 = int(input("Escriba el dividendo: "))
n2 = int(input("Escriba el divisor: "))

print(f'El resultado de la division es: {n1/n2:.2f}, su cociente es: {n1//n2} y su resto es: {n1%n2} ')
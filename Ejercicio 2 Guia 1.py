# Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.

#Declaracion de Variables
usuario = ""
caracteres = 0

#Cuerpo del programa
def check(num):
    if num % 2 == 0:
        print("Par")
        
    else:
        print("Impar")
        
usuario = str(input("Bienvenido, por favor escriba su nomre de usuario: "))
caracteres = int(len(usuario))
print("Su nombre de usuario posee", caracteres, "caracteres")

check(caracteres)
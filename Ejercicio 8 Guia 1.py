"""
Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.
"""

#Inicializando Variables

n1 = 0

#Cuerpo del programa

n1= int(input("Escriba un numero entero: "))

for i in range(1,11):
    print(i,"x",n1,"=",i*n1)
    


"""
Manera alternativa

n1 = 0
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n1= int(input("Escriba un numero entero: "))

for i in tabla:
    print(i,"x",n1,"=",i*n1)

"""
    
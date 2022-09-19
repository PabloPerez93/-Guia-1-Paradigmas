"""Crear un conversor de pies y pulgadas a centímetros."""

#Inicializando variables

pies = 0
pulgadas = 0
centimetros = 0
opc = ""


#Cuerpo del programa

print("Bienvenido al conversor de medidas")

opc = str(input("Para convertir pies a cms presione 1. Para convertir pulgadas a cms presione 2. Para salir presione 3: "))


while opc != "0":
    if opc ==  "1":
        pies = float(input("Indique la cantidad de pies a convertir: "))
        centimetros = pies * 30.48
        print(f'Equivale a {centimetros:.2f} centimetros')
        opc = str(input("Para convertir pies a cms presione 1. Para convertir pulgadas a cms presione 2. Para salir presione 3: "))
        
    elif opc == "2":
        pulgadas = float(input("Indique la cantidad de pulgadas a convertir: "))    
        centimetros = pulgadas * 2.54
        print(f'Equivale a {centimetros:.2f} centimetros')    
        opc = str(input("Para convertir pies a cms presione 1. Para convertir pulgadas a cms presione 2. Para salir presione 3: "))

    elif opc == "3":
        print("Adios")
        break
        
    else:
        print("Error, elija una opcion valida")
        opc = str(input("Para convertir pies a cms presione 1. Para convertir pulgadas a cms presione 2. Para salir presione 3: "))
"""Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual."""

#Inicializando variables

pesos = 0
dolares = 0
selec = ""
total = 0
valor_dolar = 0


#Cuerpo de programa

print("Bienvenido al conversor de moneda")

valor_dolar = int(input("ingrese el valor del dolar a usar de referencia para la conversion: "))
selec = str(input("Presione 1 para convertir pesos, presione 2 para convertir dolares o presione 3 para salir: "))

while selec != "0":
    if selec == "1":
        pesos = int(input("Cantidad de pesos a convertir: "))
        total = pesos / valor_dolar
        print(f'El total es de {total:.2f} dolares')
        selec = str(input("Presione 1 para convertir pesos, presione 2 para convertir dolares o presione 3 para salir: "))
    
    elif selec == "2":
        dolares = int(input("Cantidad de dolares a convertir: "))
        total = dolares * valor_dolar
        print(f'El total es de {total:.2f} pesos')
        selec = str(input("Presione 1 para convertir pesos, presione 2 para convertir dolares o presione 3 para salir: "))
        
    elif selec == "3":
            print("Adios")
            break
        
    else:
        print("Error, elija una opcion valida")
        selec = str(input("Presione 1 para convertir pesos, presione 2 para convertir dolares o presione 3 para salir. "))
        
        
        
            
        
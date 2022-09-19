"""Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaría la tarjeta de bingo de una persona. Una vez generado los números aleatorios solicitar al usuario que ingrese 3 números enteros, a parƟr de allí mostrar los siguientes mensajes: Si el usuario no marcó ninguno de los números, indicarlo diciendo “El jugador tiene mala suerte, no marcó ninguna casilla”. Caso contrario mostrar “El jugador marcó algún número de la tarjeta”"""
    
#Inicializando variables
eleccion = []
numeros = []


import random

numeros =  set(random.sample(range(1, 100), 15))

eleccion = set([int(input("Elegi 3 nums del 1 al 100: ")) for valor in range(3)])

comparacion = numeros & eleccion

if len(comparacion) > 0:
    print(f'Hay {len(comparacion)} numeros coincidientes!')
    print(f'Los numeros coincidentes son: {comparacion}'.replace("{","").replace("}",""))
else:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")







    
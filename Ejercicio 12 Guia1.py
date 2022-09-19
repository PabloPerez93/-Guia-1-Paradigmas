"""Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido,
si se pide en cada mes el 10% del sueldo ganado."""

#Inicializando variables

sueldo = 1.0
ahorro = 0
mes = 0

#Cuerpo del programa


while mes < 12:
    sueldo = float(input("Ingrese su sueldo neto del mes: "))
    ahorro += (sueldo * 10) / 100
    mes += 1

print(f'Anualmente tendria un ahorro de ${ahorro:.2f} pesos si deposita el 10% de su sueldo mensualmente')




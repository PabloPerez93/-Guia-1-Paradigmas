"""Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora."""

#Inicializando Variables

opc = ""
horas_trabajadas = 0
pago_total = 0.0

#Variables constantes

PRECIO_NOCTURNO = 40.60
PRECIO_DIURNO = 35.50

opc = str(input("Presione 1 para horario diurno. Presione 2 para horario nocturno: "))

while opc != "0":
    if opc == "1":
        horas_trabajadas = float(input("Cuantas horas trabajó?: "))
        pago_total = horas_trabajadas * PRECIO_DIURNO
        print(f'Corresponde una remuneracion de: ${pago_total}')
        break
        
    elif opc == "2":
        horas_trabajadas = float(input("Cuantas horas trabajó?: "))
        pago_total = horas_trabajadas * PRECIO_NOCTURNO
        print(f'Corresponde una remuneracion de: ${pago_total}')
        break
    
    else: 
        print("Error, elija una opcion válida.")
        opc = str(input("Presione 1 para horario diurno. Presione 2 para horario nocturno: "))
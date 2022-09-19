# Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras

#Declaracion de Variables
kg = 0.0
lb = 0.0
seleccion = 0
total = 0.0

#Variable constante
ESCALA = 2.2


#Cuerpo del programa
print("Bienvenido al conversor de unidades! Por favor, seleccione un tipo de unidad")

def selec(seleccion):
    seleccion = int(input("Presione 1 para KGS o 2 para LBS: "))
    
    if seleccion == 1:
        kg = input("Igrese kgs:  ")
        total = float(kg) * ESCALA
        print("El peso equivale a: ", "{:.2f}".format (total), "libras")
        
    elif seleccion == 2:
        lb = input("Ingrese lbs: ")
        total = float(lb) / ESCALA
        print("El peso equivale a:", "{:.2f}".format (total), "kilos")

    else:
        if seleccion >= 3:
            
           print("Error, elija una opcion valida")
           selec(seleccion)
        
selec(seleccion)
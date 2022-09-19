"""Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería: soledad.steffolani@umet.edu.ar"""

#Inicializando variables

nombre = ""
apellido = ""
dominio = ""

#Cuerpo del programa

nombre = str(input("Escriba su nombre: ").lower().replace(" ",""))
apellido = str(input("Escriba su apellido: ").lower().replace(" ",""))
dominio = str(input("Escriba su dominio de preferencia: ").lower().replace(" ",""))

if nombre[:1] == apellido[:1]:
    print(f'{nombre}.{apellido}{dominio}')
else:
    print(f'{nombre}{apellido}{dominio}')
    
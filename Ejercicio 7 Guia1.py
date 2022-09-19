#Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? 
#¿Y cómo obtendría los dos últimos dígitos? 
#Desarrolle un programa que cargue un número entero por teclado, #y muestre el último dígito del mismo (por un lado)
#y los dos últimos dígitos (por otro lado).

#Inicializacion de variables

num = 0
ultimo_digito = 0
ultimos_digitos = 0

#Cuerpo del programa

num = int(input("Ingrese un numero entero: "))
ultimo_digito = num % 10
ultimos_digitos = num % 100

print("El utimo digito es:",ultimo_digito,"Y los ultimos 2 digitos es:",ultimos_digitos)
#Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: 
#Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más el doble producto del primero por el segundo
#más el cuadrado del segundo.
#(a + b)2 = a**2 + 2 · a · b + b**2

#Inicializar variables

a = 0
b = 0
cuadrado_de_binomio = 0
#Cuerpo del programa

a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))

cuadrado_de_binomio = (a**2) + (2*a*b) + (b**2)

print("(a + b)^2 = a^2 + 2 · a · b + b^2 = ",cuadrado_de_binomio)


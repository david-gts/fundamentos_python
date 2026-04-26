#/Calcular la siguiente ecuación: rc(x)+x^3+4
#(Utilice función sqrt o función pow y en la cabecera del programa la librería #include<cmath>)
#Ejercicio09

import math
print("======================================")
print("     CÁLCULO DE LA ECUACIÓN")
print("======================================")
x = float(input("Ingrese el valor de x: "))
resultado = math.sqrt(x) + (x ** 3) + 4
print("--------------------------------------")
print("El resultado de la ecuación es: ", resultado)
print("======================================")

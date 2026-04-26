#Programa que permita calcular el volumen de una esfera. El usuario ingresa el valor del radio. Considerar pi=3.1416
#Ejercicio08

print("======================================")
print("     CÁLCULO DEL VOLUMEN DE UNA ESFERA")
print("======================================")
radio = float(input("Ingrese el valor del radio de la esfera: "))
pi = 3.1416
volumen = (4/3) * pi * (radio ** 3)
print("--------------------------------------")
print("El volumen de la esfera es: ", volumen, "cm³")
print("======================================")


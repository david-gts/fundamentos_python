#//Programa que determine las raíces de la ecuación de segundo grado de tipo: ax2+bx+c = 0, secuencial sin condicionales
#Ejercicio13

print("======================================")
print("     CÁLCULO DE LAS RAÍCES DE UNA ECUACIÓN DE SEGUNDO GRADO")
print("======================================")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
discriminante = (b ** 2) - (4 * a * c)
raiz1 = (-b + (discriminante ** 0.5)) / (2 * a)
raiz2 = (-b - (discriminante ** 0.5)) / (2 * a)
print("--------------------------------------")
print("Las raíces de la ecuación son: ", raiz1, "y", raiz2)
print("======================================")




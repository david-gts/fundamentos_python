#3.1.	Desarrollar un programa que permita leer dos números enteros y calcule las operaciones de  suma, resta, multiplicación, división, 
# residuo del primer número ingresado entre 2, el cuadrado del primer número, la raíz cúbica del número 1  multiplicado por 3.

#Ejercicio01

print("======================================")
print("     OPERACIONES MATEMÁTICAS BÁSICAS")
print("======================================")

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

print("--------------------------------------")

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
residuo = num1 % 2
cuadrado = num1 ** 2
raiz_cubica = (num1 ** (1/3)) * 3

print("Resultados:")
print("--------------------------------------")
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)
print("Residuo del primer número entre 2: ", residuo)
print("Cuadrado del primer número: ", cuadrado)
print("Raíz cúbica del primer número multiplicado por 3: ", raiz_cubica)
print("======================================")

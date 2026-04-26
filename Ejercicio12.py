#//Programa  que calcule el área de un triángulo en base a sus tres lados ingresados, halla perimetro
#Ejercicio12

print("======================================")
print("     CÁLCULO DEL ÁREA DE UN TRIÁNGULO")
print("======================================")
ladoUno = float(input("Ingrese la longitud del primer lado del triángulo: "))
ladoDos = float(input("Ingrese la longitud del segundo lado del triángulo: "))
ladoTres = float(input("Ingrese la longitud del tercer lado del triángulo: "))
perimetro = ladoUno + ladoDos + ladoTres
semiperimetro = perimetro / 2
area = (semiperimetro * (semiperimetro - ladoUno) * (semiperimetro - ladoDos) * (semiperimetro - ladoTres)) ** 0.5
print("--------------------------------------")
print("El área del triángulo es: ", area, " cm²")
print("======================================")


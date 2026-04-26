#//Determinar la HIPOTENUSA de un triángulo rectángulo aplicando el teorema de Pitágoras, 
#el perímetro y el área que representa, conociendo solamente el valor de sus catetos.
#Ejercicio06

print("======================================")
print("     CÁLCULO DE LA HIPOTENUSA, PERÍMETRO Y ÁREA")
print("======================================")
catetoUno = float(input("Ingrese la longitud del primer cateto: "))
catetoDos = float(input("Ingrese la longitud del segundo cateto: "))
hipotenusa = (catetoUno ** 2 + catetoDos ** 2) ** 0.5
perimetro = catetoUno + catetoDos + hipotenusa
area = (catetoUno * catetoDos) / 2
print("--------------------------------------")
print("La hipotenusa del triángulo rectángulo es: ", hipotenusa)
print("El perímetro del triángulo rectángulo es: ", perimetro)
print("El área del triángulo rectángulo es: ", area, " cm²")
print("======================================")
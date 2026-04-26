#Distribuir una cantidad expresada en nuevos soles, en billetes de 20, 10, 5 y 1 sol 
#Ejercicio07

print("======================================")
print("     DISTRIBUCIÓN DE BILLETES")
print("======================================")
cantidad = int(input("Ingrese la cantidad en nuevos soles: "))
billetes_20 = cantidad // 20
cantidad = cantidad % 20
billetes_10 = cantidad // 10
cantidad = cantidad % 10
billetes_5 = cantidad // 5
cantidad = cantidad % 5
billetes_1 = cantidad // 1
print("--------------------------------------")
print("Cantidad de billetes de 20 soles: ", billetes_20)
print("Cantidad de billetes de 10 soles: ", billetes_10)
print("Cantidad de billetes de 5 soles: ", billetes_5)
print("Cantidad de billetes de 1 sol: ", billetes_1)
print("======================================")


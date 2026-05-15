#Proyecto productivo IDL02
#Autores:
#DAVID RICHARD GUTIERREZ CARCAUSTO
#WANSHI JOSE REYMUNDO CALDERON
#RODRIGO CARHUALLANQUI REMUZGO


#Ejercicio practico - Ticket de préstamo de libro 
#Realizar un ticket de entrega, de una biblioteca sobre el prestamo de un libro
#Considerar los siguientes datos:
#Nombre del cliente, DNI, Titulo del libro, Autor del libro, Fecha de prestamo, Fecha de devolucion
#Considerar que el precio del libro es de 50 soles, y la multa por dia de retraso es de 5 soles,
#considerar ingresar todos los datos en la salidad de datos.

#importamos la libreria datetime para obtener la fecha actual y formatearla.
from datetime import datetime

print(":::::::::::::::::::::::::::::::::::::::::::")
print("::::::::Ticked de prestamo de libro::::::::")
print(":::::::::::::::::::::::::::::::::::::::::::")
print()

#Generacion de data de libros.
libro1 = "Aprendiendo JavaScript"
autorLibro1 = "David Flanagan"
libro2 = "Java: A Beginner's Guide"
autorLibro2 = "Herbert Schildt"
libro3 = "PostgreSQL: Up and Running"
autorLibro3 = "Regina Obe, Leo Hsu"
libro4 = "Learning React"
autorLibro4 = "Alex Banks, Eve Porcello"
libro5 = "Eloquent JavaScript"
autorLibro5 = "Marijn Haverbeke"
libro6 = "Effective Java"
autorLibro6 = "Joshua Bloch"


#Generacion de data restante del ticket
#usamos la libreria datetime para la fecha actual.
fechaPrestamo = datetime.now()
multaPorDia = 5.00

#Declaracion de variables para almacenar los datos del cliente y el libro seleccionado.
nombreCliente = input("Ingrese los nombres del cliente: ")
print()
apellidoCliente = input("Ingrese los apellidos del cliente: ")
print()
dni = input("Ingrese el DNI del cliente: ")
print()
#Validacion de datos, usamos el metodo exit() para finalizar el proceso.
#Usamos el metodo len() para validar la longitud del DNI
if len(dni) != 8:
    print("El DNI debe contener 8 caracteres Ejm: 12345678, reinicie el programa e ingrese un DNI valido.")
    exit()
libroSeleccionado = ""
autorSeleccionado = ""

#menu de libros
#Usamos f-strings para mostrar variables dentro de los print y mejorar la legibilidad del codigo.
print(":::::::::::::::::::::::::::::::::::::")
print(":::::::: Libros disponibles::::::::::")
print(":::::::::::::::::::::::::::::::::::::")
print(f"1. {libro1} - {autorLibro1}")
print(f"2. {libro2} - {autorLibro2}")
print(f"3. {libro3} - {autorLibro3}")
print(f"4. {libro4} - {autorLibro4}")
print(f"5. {libro5} - {autorLibro5}")
print(f"6. {libro6} - {autorLibro6}")
print(":::::::::::::::::::::::::::::::::::::")
opcionLibro = int(input("Seleccione el libro que desea prestar (1-6): "))

print()
#Validacion de datos, usamos el metodo exit() para finalizar el proceso.
fechaDevolucion = input("Ingrese la fecha de devolucion expresada en (dd/mm/yyyy): ")

if fechaDevolucion.count("/") != 2:
    print("Formato de fecha no valido, reinicie el programa e ingrese una fecha valida.")
    exit()

# convertir string a datetime
fechaDevolucion_dt = datetime.strptime(fechaDevolucion, "%d/%m/%Y")

if fechaDevolucion_dt < fechaPrestamo:
    print("La fecha de devolucion no puede ser anterior a la fecha de prestamo, reinicie el programa e ingrese una fecha valida.")
    exit()

#Usamos match y generacion de ticket por libro seleccionado.
match opcionLibro:
    case 1:
        libroSeleccionado = libro1
        autorSeleccionado = autorLibro1
        #Salida de datos
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                   BIBLIOTECA MUNICIPAL                   ║")
        print("║                    TICKET DE PRÉSTAMO                    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Cliente            : {nombreCliente} {apellidoCliente}")
        print(f"║ DNI                : {dni}")
        print(f"║ Libro seleccionado : {libroSeleccionado}")
        print(f"║ Autor              : {autorSeleccionado}")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Fecha préstamo     : {fechaPrestamo.strftime('%d/%m/%Y')}")
        print(f"║ Fecha devolución   : {fechaDevolucion_dt.strftime('%d/%m/%Y')}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Estado del préstamo: ACTIVO                              ║")
        print("║ Código préstamo    : PREST-001                           ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ INFORMACIÓN ADICIONAL                                    ║")
        print(f"║ Precio del libro   : S/ 50.00")
        print(f"║ Multa por retraso  : S/ {multaPorDia}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Instrucciones:                                           ║")
        print("║ - Devuelva el libro en la fecha indicada.                ║")
        print("║ - En caso de retraso, se aplicará la multa por día.      ║")
        print("║ - Para consultas, contacte a la biblioteca.              ║")
        print("║ - Teléfono: 123-456-789                                  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║                                                          ║")
        print("║         Gracias por utilizar nuestros servicios.         ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")

    case 2:
        libroSeleccionado = libro2
        autorSeleccionado = autorLibro2
        #Salida de datos
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                   BIBLIOTECA MUNICIPAL                   ║")
        print("║                    TICKET DE PRÉSTAMO                    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Cliente            : {nombreCliente} {apellidoCliente}")
        print(f"║ DNI                : {dni}")
        print(f"║ Libro seleccionado : {libroSeleccionado}")
        print(f"║ Autor              : {autorSeleccionado}")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Fecha préstamo     : {fechaPrestamo.strftime('%d/%m/%Y')}")
        print(f"║ Fecha devolución   : {fechaDevolucion_dt.strftime('%d/%m/%Y')}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Estado del préstamo: ACTIVO                              ║")
        print("║ Código préstamo    : PREST-001                           ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ INFORMACIÓN ADICIONAL                                    ║")
        print(f"║ Precio del libro   : S/ 50.00")
        print(f"║ Multa por retraso  : S/ {multaPorDia}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Instrucciones:                                           ║")
        print("║ - Devuelva el libro en la fecha indicada.                ║")
        print("║ - En caso de retraso, se aplicará la multa por día.      ║")
        print("║ - Para consultas, contacte a la biblioteca.              ║")
        print("║ - Teléfono: 123-456-789                                  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║                                                          ║")
        print("║         Gracias por utilizar nuestros servicios.         ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")   
    case 3:
        libroSeleccionado = libro3
        autorSeleccionado = autorLibro3
        #Salida de datos
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                   BIBLIOTECA MUNICIPAL                   ║")
        print("║                    TICKET DE PRÉSTAMO                    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Cliente            : {nombreCliente} {apellidoCliente}")
        print(f"║ DNI                : {dni}")
        print(f"║ Libro seleccionado : {libroSeleccionado}")
        print(f"║ Autor              : {autorSeleccionado}")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Fecha préstamo     : {fechaPrestamo.strftime('%d/%m/%Y')}")
        print(f"║ Fecha devolución   : {fechaDevolucion_dt.strftime('%d/%m/%Y')}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Estado del préstamo: ACTIVO                              ║")
        print("║ Código préstamo    : PREST-001                           ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ INFORMACIÓN ADICIONAL                                    ║")
        print(f"║ Precio del libro   : S/ 50.00")
        print(f"║ Multa por retraso  : S/ {multaPorDia}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Instrucciones:                                           ║")
        print("║ - Devuelva el libro en la fecha indicada.                ║")
        print("║ - En caso de retraso, se aplicará la multa por día.      ║")
        print("║ - Para consultas, contacte a la biblioteca.              ║")
        print("║ - Teléfono: 123-456-789                                  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║                                                          ║")
        print("║         Gracias por utilizar nuestros servicios.         ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
    case 4:
        libroSeleccionado = libro4
        autorSeleccionado = autorLibro4
        #Salida de datos
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                   BIBLIOTECA MUNICIPAL                   ║")
        print("║                    TICKET DE PRÉSTAMO                    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Cliente            : {nombreCliente} {apellidoCliente}")
        print(f"║ DNI                : {dni}")
        print(f"║ Libro seleccionado : {libroSeleccionado}")
        print(f"║ Autor              : {autorSeleccionado}")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Fecha préstamo     : {fechaPrestamo.strftime('%d/%m/%Y')}")
        print(f"║ Fecha devolución   : {fechaDevolucion_dt.strftime('%d/%m/%Y')}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Estado del préstamo: ACTIVO                              ║")
        print("║ Código préstamo    : PREST-001                           ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ INFORMACIÓN ADICIONAL                                    ║")
        print(f"║ Precio del libro   : S/ 50.00")
        print(f"║ Multa por retraso  : S/ {multaPorDia}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Instrucciones:                                           ║")
        print("║ - Devuelva el libro en la fecha indicada.                ║")
        print("║ - En caso de retraso, se aplicará la multa por día.      ║")
        print("║ - Para consultas, contacte a la biblioteca.              ║")
        print("║ - Teléfono: 123-456-789                                  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║                                                          ║")
        print("║         Gracias por utilizar nuestros servicios.         ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
    case 5:
        libroSeleccionado = libro5
        autorSeleccionado = autorLibro5
        #Salida de datos
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                   BIBLIOTECA MUNICIPAL                   ║")
        print("║                    TICKET DE PRÉSTAMO                    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Cliente            : {nombreCliente} {apellidoCliente}")
        print(f"║ DNI                : {dni}")
        print(f"║ Libro seleccionado : {libroSeleccionado}")
        print(f"║ Autor              : {autorSeleccionado}")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Fecha préstamo     : {fechaPrestamo.strftime('%d/%m/%Y')}")
        print(f"║ Fecha devolución   : {fechaDevolucion_dt.strftime('%d/%m/%Y')}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Estado del préstamo: ACTIVO                              ║")
        print("║ Código préstamo    : PREST-001                           ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ INFORMACIÓN ADICIONAL                                    ║")
        print(f"║ Precio del libro   : S/ 50.00")
        print(f"║ Multa por retraso  : S/ {multaPorDia}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Instrucciones:                                           ║")
        print("║ - Devuelva el libro en la fecha indicada.                ║")
        print("║ - En caso de retraso, se aplicará la multa por día.      ║")
        print("║ - Para consultas, contacte a la biblioteca.              ║")
        print("║ - Teléfono: 123-456-789                                  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║                                                          ║")
        print("║         Gracias por utilizar nuestros servicios.         ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
    case 6:
        libroSeleccionado = libro6
        autorSeleccionado = autorLibro6
        #Salida de datos
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                   BIBLIOTECA MUNICIPAL                   ║")
        print("║                    TICKET DE PRÉSTAMO                    ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Cliente            : {nombreCliente} {apellidoCliente}")
        print(f"║ DNI                : {dni}")
        print(f"║ Libro seleccionado : {libroSeleccionado}")
        print(f"║ Autor              : {autorSeleccionado}")
        print("╠══════════════════════════════════════════════════════════╣")
        print(f"║ Fecha préstamo     : {fechaPrestamo.strftime('%d/%m/%Y')}")
        print(f"║ Fecha devolución   : {fechaDevolucion_dt.strftime('%d/%m/%Y')}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Estado del préstamo: ACTIVO                              ║")
        print("║ Código préstamo    : PREST-001                           ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ INFORMACIÓN ADICIONAL                                    ║")
        print(f"║ Precio del libro   : S/ 50.00")
        print(f"║ Multa por retraso  : S/ {multaPorDia}")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║ Instrucciones:                                           ║")
        print("║ - Devuelva el libro en la fecha indicada.                ║")
        print("║ - En caso de retraso, se aplicará la multa por día.      ║")
        print("║ - Para consultas, contacte a la biblioteca.              ║")
        print("║ - Teléfono: 123-456-789                                  ║")
        print("╠══════════════════════════════════════════════════════════╣")
        print("║                                                          ║")
        print("║         Gracias por utilizar nuestros servicios.         ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
    case _:
        print("Opcion no valida, reinicie el programa y seleccione una opcion valida.")









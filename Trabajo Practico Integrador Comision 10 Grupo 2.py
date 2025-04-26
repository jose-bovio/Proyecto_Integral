#Trabajo Integrador Matematica
#Comision 10 grupo 2
#Alumnos: Batista Federico, Benitez Rodrigo, Bertotti Franco, Bovio Jose, Caballero Myriam
numero = int(input("Ingresa un numero entero positivo: "))
if numero < 0:
    print("El número debe ser positivo. Intenta nuevamente.")
else:
    print("Este programa pasa un numero decimal a binario, octal, o hexadecinmal")
    print("Seleciona una opcion")
    print("decimal a binario:1")
    print("decimal a octal: 2")
    print("decimal a hexadecimal: 3")
    opcion = int(input("Ingrese una opcion: "))
    match opcion:
        case 1:
        #AL NUMERO ENTERO LO CONVIERTE A BINARIO
            potencia = 1
            acumulador = 0
            cociente = numero        
            while cociente != 0:
                resto = cociente % 2            
                cociente = cociente // 2           
                acumulador = resto * potencia + acumulador
                potencia = potencia * 10
            print(f"El numero decimal {numero}, es equivalente al numero binario {acumulador}")
        case 2:
        #AL NUMERO ENTERO LO CONVIERTE A OCTAL
            potencia = 1
            acumulador = 0         
            cociente = numero        
            while cociente != 0:
                resto = cociente % 8            
                cociente = cociente // 8           
                acumulador = resto * potencia + acumulador
                potencia = potencia * 10
            print(f"El numero decimal {numero}, es equivalente al numero octal {acumulador}")
        case 3:
        #AL NUMERO ENTERO LO CONVIERTE A HEXADECIMAL
            acumulador = ""
            hexa = "0123456789ABCDEF"         
            cociente = numero        
            while cociente != 0:
                resto = cociente % 16            
                cociente = cociente // 16           
                acumulador = hexa [resto] + acumulador           
            print(f"El numero decimal {numero}, es equivalente al numero hexadecimal {acumulador}")
        case _:
            print("no corresponde a una opcion, vuelve a intentar")
    print("Fin del programa")
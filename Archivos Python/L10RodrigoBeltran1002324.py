print("Semana No. 10: Ejercicio 1")
mesEntrada = int(input("Ingrese un número de 1-12: "))

match mesEntrada: 
    
    case 1: 
        mesSalida = "Enero"
    case 2: 
        mesSalida = "Febrero"
    case 3: 
        mesSalida = "Marzo"
    case 4: 
        mesSalida = "Abril"
    case 5: 
        mesSalida = "Mayo"
    case 6: 
        mesSalida = "Junio"
    case 7: 
        mesSalida = "Julio"
    case 8: 
        mesSalida = "Agosto"
    case 9: 
        mesSalida = "Septiembre"
    case 10: 
        mesSalida = "Octubre"
    case 11: 
        mesSalida = "Noviembre"
    case 12: 
        mesSalida = "Diciembre"
    case _:
        print("Error: El número a ingresar debe estar contenido entre 1 y 12")

print(f"MES:  {mesSalida}")


print("Semana No. 10: Ejercicio 2")
a = int(input("Ingrese un primer número positivo: "))
b = int(input("Ingrese un segundo número positivo: "))
c = int(input("Ingrese un tercer número positivo: "))

if(a <= 0 or b <= 0 or c <= 0):
    print("Error, el número debe ser mayor a cero")

if(a > b): 
    if (a > c):
        print("El número A es mayor que B y C")
    else: 
        if (a == c):
            print("A es mayor a B y A es igual a C")
        else: 
            print("A es mayor que B y A es diferente a C")
else:
    if (a == b):
        if(a > c):
            print("A es mayor que C y A es igual a B")
        else:
            if(a == c):
                print("A es menor o igual que B, A es igual a B y A es igual a C")
            else:
                print("A es menor o igual que B, A no es igual a B y A no es igual a C")

    else:
        if(b > c):
            print("A es menor o igual que B, B es mayor que C")
        else:
            if(b == c):
                print("A es menor o igual que B, B es igual a C")
            else: 
                print("A es menor o igual que B, B no es igual a C")

print("\nCarlos Rodrigo Beltran Tello - 1002324")
dia_nacimiento = int(input("Ingrese su día de nacimiento (1-31): "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento (1-12): "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

if(dia_nacimiento >= 1 and dia_nacimiento <=31): 
    if(mes_nacimiento >= 1 and mes_nacimiento <=12):
            if (mes_nacimiento == 1):
                if (dia_nacimiento <= 19):
                    signo = "Capricornio"
                else:
                    signo = "Acuario"
            elif (mes_nacimiento == 2):
                if (dia_nacimiento <= 18):
                    signo = "Acuario"
                elif(dia_nacimiento > 18 and dia_nacimiento <=29):
                    signo = "Piscis"
                else:
                    print("Día de nacimiento inválido. Febrero tiene máximo 29 días!!")
            elif (mes_nacimiento == 3):
                if (dia_nacimiento <= 20):
                    signo = "Piscis"
                else:
                    signo = "Aries"
            elif (mes_nacimiento == 4):
                if (dia_nacimiento <= 20):
                    signo = "Aries"
                else:
                    signo = "Tauro"
            elif (mes_nacimiento == 5):
                if (dia_nacimiento <= 20):
                    signo = "Tauro"
                else:
                    signo = "Géminis"
            elif (mes_nacimiento == 6):
                if (dia_nacimiento <= 20):
                    signo = "Géminis"
                else:
                    signo = "Cáncer"
            elif (mes_nacimiento == 7):
                if (dia_nacimiento <= 22):
                    signo = "Cáncer"
                else:
                    signo = "Leo"
            elif (mes_nacimiento == 8):
                if (dia_nacimiento <= 22):
                    signo = "Leo"
                else:
                 signo = "Virgo"
            elif (mes_nacimiento == 9):
                if (dia_nacimiento <= 22):
                    signo = "Virgo"
                else:
                    signo = "Libra"
            elif (mes_nacimiento == 10):
                if (dia_nacimiento <= 23):
                    signo = "Libra"
                else:
                    signo = "Escorpio"
            elif (mes_nacimiento == 11):
                if (dia_nacimiento <= 22):
                    signo = "Escorpio"
                else:
                    signo = "Sagitario"
            elif (mes_nacimiento == 12):
                if (dia_nacimiento <= 21):
                    signo = "Sagitario"
                else:
                    signo = "Capricornio"
    else:
        print("ERROR. El mes de nacimiento es inválido. Ingrese un número entre 1 y 12.")
else:
    print("ERROR. El día de nacimiento es inválido. Ingrese un número entre 1 y 31.")

print(f"Tu signo es: {signo}")
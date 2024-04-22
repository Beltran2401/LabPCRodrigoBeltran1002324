print("NÚMERO PERFECTO\n")

numero = int(input("Ingrese un número positivo -> "))

def numero_perfecto(num): 
    n = num
    divisores = 0

    for i in range (1, n): 
        if (n % i == 0): 
            divisores += i
    
    if (divisores == n): 
        print("SÍ es número perfecto :)")
    else: 
        print("NO es número perfecto :(")

numero_perfecto(numero)
print("Semana No.11: Ejercicio 1")

n = int(input("Ingrese un número mayor a cero -> "))

if(n<=0): 
    print("Eror, debe ser mayor a cero")

#Definición de Variables de Fibonacci
a = 0
b = 1
c = 0

i = 2
resultado = ""

if (n>0): 
    resultado = str(a)

    if(n > 1): 
        resultado = resultado + " , " +  str(b)
    
    while(i < n): 
        c = a + b
        resultado = resultado + " , " + str(c)
        a = b
        b = c

        i+=1
    
    print(resultado)
else: 
    print(resultado)

#EJERCICIO 2
print("\n\nSemana No.11: Ejercicio 2")

n2 = int(input("Ingrese un número mayor a cero -> "))

if(n2<=0): 
    print("Eror, debe ser mayor a cero")
#Problema A
calculoA = 0
for xA in range(1, n2 + 1): 
    calculoA += 1/xA

print ("El resultado de A es: ", calculoA)

#Problema B
calculoB = 0
for xB in range(1, n2 + 1): 
    calculoB += 1 / pow(2, xB)

print("El resultado de B es: ", calculoB)

#Problema C
resultado_preguntaNum = int(input("\n¿Desea utilizar el último número ingresado como 'n' para la sumatoria? 1 = Sí/ 0 = No -> "))
while True:

    if(resultado_preguntaNum == 1):
        n3 = n2
        x = int(input("\nIngrese el valor de 'x' para realizar la Sumatoria -> "))
        a = int(input("Ingrese el valor de 'a' para realizar la Sumatoria -> "))
        break
    elif(resultado_preguntaNum == 0): 
        n3 = int(input("\nIngrese el valor de 'n' para realizar la sumatoria -> "))
        if(n3 > 0): 
            x = int(input("Ingrese el valor de 'x' para realizar la Sumatoria -> "))
            a = int(input("Ingrese el valor de 'a' para realizar la Sumatoria -> "))
            break
        else: 
            print("Ingrese un número positivo. Error.")
    else: 
        print("Error. Ingrese una opción válida.")


calculoC = 0
for k in range(0, n3+1): 
    calculoC += pow(x, k) * pow(a, n3-k)

print("\nEl resultado de C es: ", calculoC)

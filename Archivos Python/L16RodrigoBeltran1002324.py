import random

print("Semana No. 16: Ejercicio 1")

lista = []

for x in range (10): 
    lista.append(random.randint(0, 10))

opcion = 'a'

while (opcion != 'e'): 

    print("MENÚ:")
    print("a. Mostrar números", "b. Promedio", "c. Longitud", "d. Posición", sep="\n")
    opcion = input("Ingrese una opcion -> ")

    match opcion:

        case 'a': 

            for x in range(len(lista)): 
                print(f"No. {x}: {lista[x]}")

        case 'b': 
            promedio = 0
            sumatoria = 0

            for y in range(len(lista)): 
                sumatoria += lista[y]

            promedio = sumatoria / len(lista)

            print(f"El promedio del arreglo es: {promedio}")

        case 'c': 
            print(f"La longitud del arreglo es: {len(lista)}")

        
        case 'd': 
            sumaPares = 0
            sumaImpares = 0

            for z in range(len(lista)): 
                if (z % 2 == 0): 
                    sumaPares += lista[z]
                else: 
                    sumaImpares += lista[z]

            
            print(f"La Suma de Pares es: {sumaPares}", f"La suma de Impares es: {sumaImpares}", sep= "\n")


print("Semana No. 16: Ejercicio 2")

filas = 0
columnas = 0

filas = int(input("Ingrese la cantidad de filas -> "))
columnas = int(input("Ingrese la cantidad de columnas -> "))

matriz = [[0 for x in range(columnas)] for y in range(filas)]

mayor = 0
cantidadPar = 0
cantidadImpar = 0
menor = 1000

for xFilas in range(filas): 
    for yColumnas in range (columnas): 

        matriz[xFilas][yColumnas] = random.randint(0, 1000)

        if (matriz[xFilas][yColumnas] >= mayor):
            mayor = matriz[xFilas][yColumnas]

        if (matriz[xFilas][yColumnas] <= menor): 
            menor = matriz[xFilas][yColumnas]

        if (matriz[xFilas][yColumnas] % 2 == 0): 
            cantidadPar += 1
        else: 
            cantidadImpar += 1

print(matriz)
print(f"El número mayor es: {mayor}", f"El número menor es: {menor}", f"La cantidad de Pares: {cantidadPar}", f"La cantidad de Impares: {cantidadImpar}", sep="\n")
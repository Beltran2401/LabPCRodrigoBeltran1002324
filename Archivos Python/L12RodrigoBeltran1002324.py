print("Semana No. 12: Ejercicio 1\n")
print("Menú", "a. Sumatoria", "b. Factorial", "c. Tablas de Multiplicar", "d. Número perfecto", sep="\n")

opcion = input("\nIngrese su opción -> ")

while True: 
    match opcion: 
        case "a": 
            n = int(input("Ingrese un número entero positivo -> "))

            if (n <= 0): 
                print("Error, el número debe ser mayor a cero.")

            contador = 1
            sumatoria = 0
            while(contador <= n):
                sumatoria += contador
                contador += 1

            print(f"Sumatoria: {sumatoria}")
            break

        case "b": 
            n = int(input("Ingrese un número entero mayor o igual a cero -> "))

            if (n < 0): 
                print("Error, el número debe ser mayor a cero.")
        
            i = 1
            factorial = 1
            while i <= n: 
                factorial *= i
                i += 1

            print(f"Factorial: {factorial}")
            break
    
        case "c": 
            tituloCol = "\t"
            for columnas in range (1, 11):
                tituloCol += str(columnas) + "\t"

            print (tituloCol)

            textoFila = ""
            for fila in range (1, 11): 
                textoFila += str(fila) + "\t"
                for col in range(1, 11): 
                    textoFila += str(fila * col) + "\t"

                print (textoFila)
                textoFila = ""
            break

        case _:
            print("Error. Opción Inválida.")
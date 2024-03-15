#EJERCICIO 1 - ACTIVIDAD NO. 02
print("Ejercicio 1: operaciones aritméticas")

#Entradas
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))

#Operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
divisionEntera = numero1 // numero2
divisionModular = numero1 % numero2

#Salidas
print(numero1, " + ", numero2, " = ", suma)
print(numero1, " - ", numero2, " = ", resta)
print(numero1, " * ", numero2, " = ", multiplicacion)
print(numero1, " // ", numero2, " = ", divisionEntera)
print(numero1, " % ", numero2, " = ", divisionModular)

#EJERCICIO 2 - ACTIVIDAD NO. 02
print("\nEjercicio 2: operaciones booleanas")

#Operaciones
mayor = numero1 > numero2
menor = numero1 < numero2
igualdad = numero2 == numero1
diferencia = numero1 != numero2

#Salidas
print(numero1, " > ", numero2, " = ", mayor)
print(numero1, " < ", numero2, " = ", menor)
print(numero1, " == ", numero2, " = ", igualdad)
print(numero1, " != ", numero2, " = ", diferencia)

#EJERCICIO 3 - ACTIVIDAD NO. 02
print("\nEjercicio 3: jerarquía de operadores")

#Entradas
a = int(input("Ingrese un primer número entero: "))
b = int(input("Ingrese un segundo número entero: "))
c = int(input("Ingrese un tercer número entero: "))

#Operaciones
oper1 = (a*b) + c
oper2 = (b+c) * a
oper3 = a / (b+c)
oper4 = ((3*a) + (2 * b)) / (c * c)

#Salidas
print("a * b + c =", oper1)
print("a(b+c) =", oper2)
print("a / (b + c) =", oper3)
print("(3a + 2b) / (c^2) = ", oper4)

#EJERCICIO - ACTIVIDAD NO. 03
#Análisis: 

#Encabezado
print("\nCarlos Beltran - 1002324")

#Entrada: Cantidad en m (metros)
metros = float(input("Ingrese una cantidad en metros (m): "))

#Proceso: Multiplicar o dividir la cantidad en metros por su respectivo factor de conversión, 
#para obtener el resultado en millas, kilometros, pies y pulgadas.

millas = metros / 1609
kilometros = metros / 1000
pies = metros * 3.28084
pulgadas = metros * 39.3701

#Salida: Cantidad en millas (mi), kilometros (km), pies (ft) y pulgadas (in)
print("Resultado: \n")
print("Millas:", millas)
print ("Kilometros:", kilometros)
print("Pies:", pies)
print("Pulgadas:", pulgadas)

#EJERCICIO 1
print("Ejercicio 1: operaciones aritméticas")

#Entradas
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))

#Operaciones
suma = numero1 + numero2
resta = numero1 + numero2
multiplicacion = numero1 * numero2
divisionEntera = numero1 // numero2
divisionModular = numero1 % numero2

#Salidas
print(numero1, " + ", numero2, " = ", suma)
print(numero1, " - ", numero2, " = ", resta)
print(numero1, " * ", numero2, " = ", multiplicacion)
print(numero1, " // ", numero2, " = ", divisionEntera)
print(numero1, " % ", numero2, " = ", divisionModular)

#EJERCICIO 2
print("Ejercicio 2: operaciones booleanas")

#Operaciones
mayor = numero1 > numero2
menor = numero1 < numero2
igualdad = numero2 == numero2
diferencia = numero1 != numero2

#Salidas
print(numero1, " > ", numero2, " = ", mayor)
print(numero1, " < ", numero2, " = ", menor)
print(numero1, " == ", numero2, " = ", igualdad)
print(numero1, " != ", numero2, " = ", diferencia)

#EJERCICIO 3
print("Ejercicio 3: jerarquía de operadores")

#Entradas
a = int(input("Ingrese un primer número entero: "))
b = int(input("Ingrese un segundo número entero: "))
c = int(input("Ingrese un tercer número entero: "))

oper1 = (a*b) + c
oper2 = (b+c) * a
oper3 = a / (b+c)
oper4 = ((3*a) + (2 * b)) / (c * c)
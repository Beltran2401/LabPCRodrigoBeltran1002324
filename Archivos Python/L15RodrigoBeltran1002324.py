#ACTIVIDAD NO. 01
import math
opcion1 = ''

def ObtenerAreaTriangulo (base, altura): 
    area = (base * altura) / 2
    return area

def ObtenerAreaCuadrado (lado): 
    area = math.pow(lado, 2)
    return area

def ObtenerAreaRectangulo (base, ancho): 
    area = base * ancho
    return area

def ObtenerAreaCirculo (radio): 
    area = (math.pow(radio, 2)) * math.pi
    return area

print("MENU 1")
print("a. Área de Triángulo", "b. Área de Cuadrado", "c. Área de Rectángulo", "d. Área de Círculo", sep="\t\n")
opcion1 = input("Ingrese una opción -> ")

match opcion1: 

    case 'a':
        b = float(input("Ingrese la base del triángulo -> "))
        h = float(input("Ingrese la altura del triángulo -> "))
        areaTriangulo = ObtenerAreaTriangulo(b, h)
        print(f"El área es: {areaTriangulo} u^2")
    case 'b':
        l = float(input("Ingrese el lado del cuadrado -> "))
        areaCuadrado = ObtenerAreaCuadrado(l)
        print(f"El área es: {areaCuadrado} u^2")
    case 'c':
        b = float(input("Ingrese la base del rectángulo -> "))
        a = float(input("Ingrese el ancho del rectángulo -> "))
        areaRectangulo = ObtenerAreaRectangulo(b, a)
        print(f"El área es: {areaRectangulo} u^2")
    case 'd':
        r = float(input("Ingrese el radio del círculo -> "))
        areaCirculo = ObtenerAreaCirculo(r)
        print(f"El área es: {areaCirculo} u^2")
    
    case _:
        print("Error: Ingrese una letra (a-d)")

print("")
#ACTIVIDAD NO. 02

x = 0
y = 0

def MoverPosicion(cantX, cantY):
    global x, y
    x += cantX
    y += cantY

opcion2 = 'a'

while (opcion2 != 'e'):
 print("MENÚ 2")
 print("a. Sube", "b. Baja", "c. Izquierda", "d. Derecho", "e. Salir", sep="\t\n")
 opcion2 = input("Ingrese una opción -> ")

 match opcion2: 

    case 'a':
        MoverPosicion(0, 1)
    case 'b':
        MoverPosicion(0, -1)
    
    case 'c':
        MoverPosicion(-1, 0)
    
    case 'd':
        MoverPosicion(1, 0)

    case 'e':
         print("ADIOS")
         break
    
    case _:
        print("Error: debe ingresar una letra (a-e)")

 print(f"La posición actual es [{x}][{y}]")

print(f"La posición FINAL es [{x}][{y}]")

#IMPORTAR LIBRERIAS
import re #Regex
from datetime import datetime #Datetime

#INICIALIZAR VARIABLES

#--Crear Variables Globales--
def inicializador ():
    global opcion, opcion_reporte, opcion_reporte, opcion_alumno,  id_curso, nombre_curso, horario_curso, salon_curso, catedratico_curso, notaAgregarCurso, totalAlumnos_curso, notaAcumulada, cursos, alumnos_curso, carne_alumno, nombre_alumno
    global fechaNacimiento_alumno, notaAlumno_curso, alumnos, notas_Alumno, cursosAlumno, notasAlumno, media_curso, estadoid_CursoCreado, estadoid_CursoEditado, estado_carneAlumnoCreado, estado_carneAlumnoEditado, estado_fechaAlumnoCreado
    global estado_fechaAlumnoEditado, estado_idCursoBuscado, estado_CarneAlumnoBuscado, estado_notaAlumno, estado_Opcionb, estado_Opcionc, estado_InformacionCurso, estado_InformacionAlumno, i, j, k, l, m, n, p, q, r, s

# -- Opciones --
opcion = 0
opcion_reporte = 0
opcion_alumno = ''

#--Cursos--
id_curso = ""
nombre_curso = ""
horario_curso = ""
salon_curso = ""
catedratico_curso = ""
notaAgregarCurso = 0.0
totalAlumnos_curso = 0
notaAcumulada = 0.0
cursos = [["1", "Pensamiento Computacional (Práctica)", "9:50 - 11:40", "T-203", "Ing. Luis Pedro Ovalle"],
          ["2", "Variable Commpleja", "8:30 - 9:50", "D-15", "Dr. Mario Ranferi"]]

alumnos_curso = [["1", "Pensamiento Computacional (Práctica)", "1", "38.75", ["1125022"], ["Maria Andreé Lopez Lozano"], ["38.75"]],
                 ["2", "Variable Compleja", "2", "160.00", ["1002324", "1125022"], ["Carlos Rodrigo Beltran Tello", "Maria Andreé Lopez Lozano"], ["80.00", "80.00"]]] #Se inicializa el array para un curso

#--Alumnos--
carne_alumno = ""
nombre_alumno = ""
fechaNacimiento_alumno = datetime.now() #Se inicializa la variable con la fecha de hoy
notaAlumno_curso = 0.0
alumnos = [["1002324", "Carlos Rodrigo Beltran Tello", "01-11-2005"], #Se inicializa el arrya con 2 alumnos
           ["1125022", "Maria Andreé Lopez Lozano", "22-07-2003"]] 
notas_Alumno = [["1002324", ["2"], ["80.00"]],
               ["1125022", ["1", "2"], ["39.75","80.00"]]] #Se inicializa el array
cursosAlumno = []
notasAlumno = []

#--Reportes--
media_curso = 0.0

#Verificaciones
estadoid_CursoCreado = True
estadoid_CursoEditado = True
estado_carneAlumnoCreado = True
estado_carneAlumnoEditado = True
estado_fechaAlumnoCreado = True
estado_fechaAlumnoEditado = True
estado_idCursoBuscado = True
estado_CarneAlumnoBuscado = True
estado_notaAlumno = True
estado_Opcionb = True
estado_Opcionc = True
estado_InformacionCurso = True
estado_InformacionAlumno = True

#--Contadores--
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
p = 0
q = 0
r = 0
s = 0

#FUNCIONES

#--Opción 1 (Crear Curso)--
def CrearCurso (): 

    print("\n¡CREAR CURSO!")

    #Incializar Variables
    estadoid_CursoCreado = True
    estado_InformacionCurso = True
    id_curso = ""
    nombre_curso = ""
    horario_curso = ""
    salon_curso = ""
    catedratico_curso = ""
    i = 0

    #Verificar el ID del Curso
    while estadoid_CursoCreado: 

        id_curso = input("\nIngrese el ID del Curso a Crear -> ")

        for i in range(0, len(cursos)): 
                if(id_curso == cursos[i][0]):
                    print("EROR. Ya existe un curso con el ID ingresado.")
                    estadoid_CursoCreado = True
                    break
                else: 
                    estadoid_CursoCreado = False

    #Verificar la Información del Curso
    while estado_InformacionCurso: 
                        nombre_curso = input("Ingrese el nombre del Curso -> ")
                        horario_curso = input("Ingrese el horario del Curso -> ")
                        salon_curso = input("Ingrese el salón donde se impartirá el Curso -> ")
                        catedratico_curso = input("Ingrese el nombre del catedrático que impartirá el curso -> ")


                        if ((re.fullmatch(r"[A-Za-zñÑáéíóúÁÉÍÓÚ¿?() ]{1,100}", nombre_curso))):

                            #Agregar Curso en las Matrices Correspondientes
                            cursos.append([id_curso, nombre_curso, horario_curso, salon_curso, catedratico_curso])
                            alumnos_curso.append([id_curso, nombre_curso, "0", "0.0", [], [], []])
                            print("CURSO CREADO")

                            print(cursos) #QUITAR
                            print(alumnos_curso)  #QUITAR

                            estado_InformacionCurso = False
                        else: 
                            print("Los datos ingresados no cumplen el formato correcto. Intente de Nuevo.")     

#--Opcion 2 (Editar Curso)--
def EditarCurso (): 

    print("\n¡EDITAR CURSO!")

    #Inicializar Variables
    estadoid_CursoEditado = True
    estado_InformacionCurso = True
    id_curso = ""
    nombre_curso = ""
    horario_curso = ""
    salon_curso = ""
    catedratico_curso = ""
    textoImprimir = ""
    i = 0
    j = 0
    k = 0

    print("\nCURSOS EXISTENTES")
    print("| ID |  | Nombre |  | Horario |  | Salón |  | Catedrático |")

    #Mostrar Cursos Existentes
    for i in range (len(cursos)): 
        textoImprimir = ""

        for j in range(len(cursos[0])):
              textoImprimir += "| " + cursos[i][j] + " |  "
        
        print(textoImprimir)

    #Verificar ID del Curso
    while estadoid_CursoEditado: 
         
        id_curso = input("\nIngrese el ID del Curso a Editar -> ")

        for k in range(len(cursos)):
             
            if (cursos[k][0] == id_curso): 
                
                #Verificar Información del Curso
                while estado_InformacionCurso: 
                        
                        nombre_curso = input("Ingrese el nombre del Curso -> ")
                        horario_curso = input("Ingrese el horario del Curso -> ")
                        salon_curso = input("Ingrese el salón donde se impartirá el Curso -> ")
                        catedratico_curso = input("Ingrese el nombre del catedrático que impartirá el curso -> ")


                        if ((re.fullmatch(r"[A-Za-zñÑáéíóúÁÉÍÓÚ¿?() ]{1,100}", nombre_curso))):
                            cursos[k][1] = nombre_curso
                            cursos[k][2] = horario_curso
                            cursos[k][3] = salon_curso
                            cursos[k][4] = catedratico_curso

                            alumnos_curso[k][1] = nombre_curso
                            #FALTA EDITAR NOMBRE EN LA MATRIZ DE ALUMNOS
                            print("CURSO EDITADO")

                            print(cursos) #QUITAR
                            print(alumnos_curso)  #QUITAR

                            estado_InformacionCurso = False
                            estadoid_CursoEditado = False
                        else: 
                            print("Los datos ingresados no cumplen el formato correcto. Intente de Nuevo.")

        if (estadoid_CursoEditado): 
            print("El curso no Existe. Inténtelo de Nuevo.")     
                
#--Opcion 3 (Control de Alumnnos)--
def ControlAlumnos (): 

    print("\n¡CONTROL ALUMNOS!")

    #Inicializar Variables
    opcion_alumno = ""
    estado_carneAlumnoCreado = True
    estado_carneAlumnoEditado = True
    estado_fechaAlumnoCreado = True
    estado_fechaAlumnoEditado = True
    estado_CarneAlumnoBuscado = True
    estado_InformacionAlumno = True
    carne_alumno = ""
    nombre_alumno = ""
    textoImprimir = ""
    fechaNacimiento_alumno = datetime.now()
    i = 0
    j = 0
    k = 0

    opcion_alumno = input("\n¿Desea Crear o Editar un Alumno? C: Crear / E: Editar -> ").upper()

    if(opcion_alumno == 'C'): 
            

            #Verificar el Carné del Alumno
            while estado_carneAlumnoCreado: 

                carne_alumno = input("\nIngrese el Carné del Alumno a Crear -> ")

                for i in range(0, len(alumnos)): 

                    if(carne_alumno == alumnos[i][0]):
                        print("EROR. Ya existe un alumno con el Carné ingresado.")
                        estado_carneAlumnoCreado= True
                        break
                    else: 
                        estado_carneAlumnoCreado = False

            #Verificar la Información del Alumno
            while estado_InformacionAlumno: 
                        
                        nombre_alumno = input("Ingrese el nombre del Alumno -> ")

                        if ((re.fullmatch(r"[A-Za-zñÑáéíóúÁÉÍÓÚ ]{1,100}", nombre_alumno))):

                            while estado_fechaAlumnoCreado: 
                                 
                                fechaNacimiento_alumno = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa) -> ")

                                if (datetime.strptime(fechaNacimiento_alumno, '%d/%m/%Y')): 

                                    if (datetime.strptime(fechaNacimiento_alumno, '%d/%m/%Y') < datetime.now()):
                                        fechaNacimiento_alumno = datetime.strptime(fechaNacimiento_alumno, '%d/%m/%Y').strftime('%d-%m-%Y')
                                        estado_fechaAlumnoCreado = False
                                        estado_InformacionAlumno = False
                                    else: 
                                        print("Ingrese una fecha Correcta.")
                                else: 
                                    print("Ingrese la fecha de Nacimiento del Alumno en el formato indicado.")
                        
                            alumnos.append([carne_alumno, nombre_alumno, fechaNacimiento_alumno])
                            notas_Alumno.append([carne_alumno, [], []])

                            print(alumnos)
                             
                        else: 
                            print("El nombre ingresado no cumple con el formato correcto. Intente de Nuevo.")
    
    elif(opcion_alumno == 'E'):
        print("\nALUMNOS EXISTENTES")
        print("| Carné |  | Nombre |  | Fecha de Nacimiento |")

        #Mostrar Alumnos Existentes
        for i in range (len(alumnos)): 
            textoImprimir = ""

            for j in range(len(alumnos[0])):
              textoImprimir += "| " + alumnos[i][j] + " |  "
        
            print(textoImprimir)

    #Verificar Carné del Alumno
        while estado_carneAlumnoEditado: 
         
            carne_alumno = input("\nIngrese el Carné del Alumno a Editar -> ")

            for k in range(len(alumnos)):
             
                if (alumnos[k][0] == carne_alumno): 
                
                    #Verificar Información del Curso
                    while estado_CarneAlumnoBuscado: 
                        
                        nombre_alumno = input("Ingrese el nombre del Alumno -> ")

                        if ((re.fullmatch(r"[A-Za-zñÑáéíóúÁÉÍÓÚ ]{1,100}", nombre_alumno))):
                            #Verificar la Fecha de Nacimiento del Alumno
                            while estado_fechaAlumnoEditado: 
                                 
                                fechaNacimiento_alumno = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa) -> ")

                                if (datetime.strptime(fechaNacimiento_alumno, '%d/%m/%Y')): 

                                    if (datetime.strptime(fechaNacimiento_alumno, '%d/%m/%Y') < datetime.now()):
                                        fechaNacimiento_alumno = datetime.strptime(fechaNacimiento_alumno, '%d/%m/%Y').strftime('%d-%m-%Y')

                                        alumnos[k][1] = nombre_alumno
                                        alumnos[k][2] = fechaNacimiento_alumno

                                        estado_fechaAlumnoEditado = False
                                        estado_carneAlumnoEditado = False
                                        estado_CarneAlumnoBuscado = False
                                        estado_InformacionAlumno = False

                                        #FALTA EDITAR LA MATRIZ DE NOTAS_ALUMNO

                                        print(alumnos) #QUITAR
                                    else: 
                                        print("Ingrese una fecha Correcta.")
                                else: 
                                    print("Ingrese la fecha de Nacimiento del Alumno en el formato indicado.")

                        else: 
                            print("Los datos ingresados no cumplen el formato correcto. Intente de Nuevo.")

        if (estado_carneAlumnoEditado): 
            print("El Alumno no Existe. Inténtelo de Nuevo.")
    else: 
        print("ERROR. Opción Inválida.")
         

#--Opcion 4 (Módulo de Calificación de Cursos)--
def CalificacionCursos ():

    print("\n¡CALIFICACIÓN DE CURSOS!")

    #Inicializar Variables
    id_curso = ""
    carne_alumno = ""
    textoImprimir = ""
    notaAlumno_curso = 0.0
    totalAlumnos_curso = 0.0
    notaAgregarCurso = 0.0
    estado_idCursoBuscado = True
    estado_CarneAlumnoBuscado = True
    estado_notaAlumno = True
    cursosAlumno = []
    notasAlumno = []
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    p = 0
    q = 0

    print("\nCURSOS EXISTENTES")
    print("| ID |  | Nombre |  | Horario |  | Salón |  | Catedrático |")

    #Mostrar Cursos Existentes
    for i in range (len(cursos)): 
        textoImprimir = ""

        for j in range(len(cursos[0])):
              textoImprimir += "| " + cursos[i][j] + " |  "
        
        print(textoImprimir)

    print("\nALUMNOS EXISTENTES")
    print("| Carné |  | Nombre |  | Fecha de Nacimiento |")

    #Mostrar Alumnos Existentes
    for k in range (len(alumnos)): 
        textoImprimir = ""

        for l in range(len(alumnos[0])):
              textoImprimir += "| " + alumnos[k][l] + " |  "
        
        print(textoImprimir)

    while estado_idCursoBuscado: 
         
        id_curso = input("\n\nIngrese el ID del Curso -> ")

        for m in range(len(cursos)):
            if (cursos[m][0] == id_curso):
                
                estado_idCursoBuscado = False

                while (estado_CarneAlumnoBuscado): 
                     
                    carne_alumno = input("Ingrese el carné del Alumno -> ")

                    for n in range(len(alumnos)): 
                        
                        if (alumnos[n][0] == carne_alumno):
                            
                            estado_CarneAlumnoBuscado = False

                            while (estado_notaAlumno):
                                
                                notaAlumno_curso = float(input("\nIngrese la nota del Alumno -> "))

                                if (notaAlumno_curso >= 0.0 and notaAlumno_curso <= 100.00):
                                    
                                    estado_notaAlumno = False

                                    for q in range(len(notas_Alumno)):
                                        
                                        if (notas_Alumno[q][0] == carne_alumno):

                                            cursosAlumno = notas_Alumno[q][1]
                                            notasAlumno = notas_Alumno[q][2]

                                            for r in range(len(cursosAlumno)):
                                                
                                                if (id_curso == cursosAlumno[r]):
                                                    
                                                    notaAgregarCurso = float(alumnos_curso[m][3])
                                                    notaAgregarCurso = notaAgregarCurso - float(notasAlumno[r])
                                                    notaAgregarCurso = notaAgregarCurso + notaAlumno_curso
                                                    notasAlumno[r] = str(notaAlumno_curso)

                                                    alumnos_curso[m][3] = str(notaAgregarCurso)
                                                    alumnos_curso[m][6][r] = str(notaAlumno_curso)

                                                    notas_Alumno[q][2] = notasAlumno

                                                    estado_notaAlumno = False
                                                
                                            if(id_curso not in cursosAlumno):

                                                totalAlumnos_curso = int(alumnos_curso[m][2])
                                                totalAlumnos_curso += 1

                                                notaAgregarCurso = float(alumnos_curso[m][3])
                                                notaAgregarCurso = notaAgregarCurso + notaAlumno_curso

                                                notasAlumno.append(str(notaAlumno_curso))

                                                notas_Alumno[q][1].append(id_curso)
                                                notas_Alumno[q][2] = notasAlumno

                                                alumnos_curso[m][2] = str(totalAlumnos_curso)
                                                alumnos_curso[m][3] = str(notaAgregarCurso)
                                                alumnos_curso[m][4].append(carne_alumno) #LO SEPARA
                                                alumnos_curso[m][5].append(alumnos[n][1])#LO SEPARA
                                                alumnos_curso[m][6].append(str(notaAlumno_curso))

                                                estado_notaAlumno = False

                        
                                else: 
                                    print("Ingrese una Nota Correcta.")

                    if (estado_CarneAlumnoBuscado): 
                        print("El alumno no Existe. Intentelo de Nuevo.")

    if (estado_idCursoBuscado == True): 
        print("El curso no Existe. Intente de Nuevo.")

    print(notas_Alumno)
    print()
    print(alumnos_curso)
    
#--Opcion 5 (Reportes)--
def Reportes (): 
    print("EN PROCESO")

#--Opcion 6 (Salir)--
def Salir (): 
    print("Muchas Gracias por hacer uso del sistema de control de notas de la Universidad Rafael Landivar. Esperamos tu experiencia haya sido la mejor. Ten un hermoso día :)")
print("CONTROL DE NOTAS UNIVERSIDAD RAFAEL LANDÍVAR (URL)")

while True: 

    print("\nMENU DE OPCIONES: ")
    print("\t1. Crear Curso", "\t2. Editar Curso", "\t3. Control de Alumnos", "\t4. Módulo de Calificación de Cursos", "\t5. Reportes", "\t6. Salir", sep="\n")

    opcion = int(input("\nIngrese una opción -> "))

    match (opcion): 

        case 1: 
            CrearCurso()
        case 2: 
            EditarCurso()
        case 3: 
            ControlAlumnos()
        case 4: 
            CalificacionCursos()
        case 5: 
            Reportes()
        case 6: 
            Salir()
            break
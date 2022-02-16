from BD.conexion import DAO
import BD.funciones
import mysql.connector
import time
import os


def limpiarPantalla():
    platform = os.name 
    if platform == 'posix':
        os.system('clear')
    elif platform == 'nt' or platform == 'ce' or platform == 'dos':
        os.system('cls')

def menuPrincipal():
    continuar = True

    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print()
            print(":=="*12+":")
            print("|\t  MENÚ PRINCIPAL"+'|'.rjust(13))
            print(":=="*12+":"+"\n")
            print("ELige una opción:".rjust(20))
            print("-----------------".rjust(20)+"\n")
            print("\t[1].Listar Estudiantes")
            print("\t[2].Registrar Estudiantes")
            print("\t[3].Promedio Final")
            print("\t[4].Actualizar Estudiantes")
            print("\t[5].Calcular Edad")
            print("\t[6].Eliminar Estudiantes")
            print("\t[7].Salir\n")

            try:
                opcion = int(input("Escribe opción (Ejemplo: 1)> "))

                if opcion < 1 or opcion > 7:
                    print("Opción incorrecta, ingrese nuevamente...")
                elif opcion == 7:
                    continuar = False
                    print("¡Gracias por usar este programa!")
                    break
                else:
                    opcionCorrecta = True
                    ejecutarOpcion(opcion)

            except ValueError as err:
                limpiarPantalla()
                print('\a')
                print("+".rjust(9)+"--"*10+"+")
                print("| ¡OPCIÓN INVALIDA!".rjust(27)+'|'.rjust(3))
                print("+".rjust(9)+"--"*10+"+")
                print("Opciones disponibles (1, 2, 3, 4, 5, 6 o 7)  ")
                time.sleep(2)
                continue

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                BD.funciones.listarCursos(cursos)
            else:
                print("No se encontraron Alumnos...")
        except:
            print("Ocurrió un error...")

    elif opcion == 2:
        curso = BD.funciones.pedirDatosRegistro()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ocurrió un error...")

    elif opcion == 3:
        cursos = dao.listarCursos()
        BD.funciones.calcularPromedio(cursos)

    elif opcion == 4:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = BD.funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except mysql.connector.Error as err:

            print("Ocurrió un error...", err)

    elif opcion == 5:
        limpiarPantalla()
        cursos = dao.listarCursos()
        if len(cursos) > 0:
            ID = BD.funciones.pedirIdEdad(cursos)
            edad = dao.traerEdad(ID)


    elif opcion == 6:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                EliminarID = BD.funciones.pedirDatosEliminacion(cursos)
                if not(EliminarID == ""):
                    dao.eliminarCurso(EliminarID)
                else:
                    print("ID de el Alumno no encontrado...\n")
            else:
                print("No se encontraron Alumnos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal();
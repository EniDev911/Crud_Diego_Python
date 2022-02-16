from BD.conexion import DAO
import BD.funciones
import mysql.connector
from dotenv import load_dotenv

dotenv_values = load_dotenv('BD/.env')

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("\n==================== MENÚ PRINCIPAL ====================")
            print("|           1.- Listar Estudiantes                     |")
            print("|           2.- Registrar Estudiantes                  |")
            print("|           3.- Promedio Final                         |")
            print("|           4.- Actualizar Estudiantes                 |")
            print("|           5.- Calcular Edad                          |")
            print("|           6.- Eliminar Estudiantes                   |")
            print("|           7.- Salir                                  |")
            print("========================================================\n")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 7:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 7:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

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
        cursos = dao.listarCursos()
        if len(cursos) > 0:
            ID = int(input("Ingrese ID: "))
            mostrar_edad = dao.calcularEdad(ID)

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
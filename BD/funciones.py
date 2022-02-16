def listarCursos(cursos):
    print("\nAlumnos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. ID: {1} | Nombre: {2} | Apellido Paterno: {3} | Apellido Materno: {4} | Notas: ({5}, {6}, {7}, {8})"
        print(datos.format(contador, cur[0], cur[1], cur[2], cur[3], cur[4], cur[5], cur[6], cur[7]))
        contador = contador + 1
    print(" ")


def pedirDatosRegistro():
    
    ID = int(input("Ingrese ID: "))
    nombre = input("Ingrese nombre: ")
    ApellidoP = input("Ingrese su apellido paterno: ")
    ApellidoM = input("Ingrese su apellido materno: ")
    FechaNac = input("Ingrese fecha de nacimiento ejemplo(1990-11-05): ")
    nota_1 = int(input("Ingrese la primera nota: "))
    nota_2 = int(input("Ingrese la segunda nota: "))
    nota_3 = int(input("Ingrese la tercera nota: "))
    nota_4 = int(input("Ingrese la cuarta nota: "))

    curso = (ID, nombre, ApellidoP, ApellidoM, FechaNac, nota_1, nota_2, nota_3, nota_4)
    return curso

def pedirDatosActualizacion(cursos):

    listarCursos(cursos)
    existeID = False
    EditarID = int(input("Ingrese el ID del curso a editar: "))
    for cur in cursos:
        if cur[0] == EditarID:
            existeID = True

    if existeID:
        nombre = input("Ingrese nombre a modificar: ")

        ApellidoP = input("Ingrese el apellido paterno a modificar: ")

        ApellidoM = input("Ingrese el apellido materno a modificar: ")
        
        FechaNac = input("Nueva fecha de nacimiento ejemplo(1990-11-05): ")

        nota_1 = int(input("Ingrese la primera nota: "))

        nota_2 = int(input("Ingrese la segunda nota: "))

        nota_3 = int(input("Ingrese la tercera nota: "))

        nota_4 = int(input("Ingrese la cuarta nota: "))

        curso = (nombre, ApellidoP, ApellidoM, nota_1, nota_2, nota_3, nota_4, EditarID)
    else:
        curso = None

    return curso

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeID = False
    EliminarID = int(input("Ingrese el ID del curso a eliminar: "))
    for cur in cursos:
        if cur[0] == EliminarID:
            existeID = True
            break

    if not existeID:
        EliminarID = ""

    return EliminarID


def calcularPromedio(cursos):
    listarCursos(cursos)

    ID = int(input("Ingrese ID: "))
    for alumno in cursos:

        if ID == alumno[0]:
            print("Calculando el promedio de {}".format(alumno[1]))
            total_notas = alumno[4] + alumno[5] + alumno[6] + alumno [7]
            promedio_final = total_notas/4
            print("Promedio final de {} es {}".format(alumno[1], promedio_final))

def pedirIdEdad(cursos):
    listarCursos(cursos)
    ID = int(input("Ingrese ID: "))
    for alumno in cursos:
        if  ID == alumno[0]:
            print("Calculando edad de {}".format(alumno[1]))
    return ID



    
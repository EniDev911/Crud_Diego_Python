import mysql.connector
from mysql.connector import Error
from mysql.connector import ProgrammingError

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='enidev911',
                db='inventario_python'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

        #finally:
         #   self.conexion.close()

    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
        self.conexion.close()

    def Notas():
        sql = "SELECT curso (nota_1, nota_2)"

    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (ID, nombre, ApellidoP, ApellidoM, nota_1, nota_2, nota_3, nota_4) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')"
                cursor.execute(sql.format(curso[0], curso[1], curso[2], curso[3], curso[4], curso[5], curso[6], curso[7]))
                self.conexion.commit()
                print("¡Alumno registrado!\n")
            except ProgrammingError as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:

                cursor = self.conexion.cursor(prepared=True)
                sql = "UPDATE `curso` SET `nombre` = ?, `apellidoP` = ?, `apellidoM` = ?, `nota_1` = ?, `nota_2` = ?, `nota_3` = ?, `nota_4` = ? WHERE `curso`.`ID` = ?"
                cursor.execute(sql, curso)
                self.conexion.commit()
                print("¡Alumno actualizado!\n")
            except ProgrammingError as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarCurso(self, IDalumnoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "delete from curso where ID = '{0}'"
                cursor.execute(sql.format(IDalumnoEliminar))
                self.conexion.commit()
                print("¡Alumno eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
     def calcularEdad(self, idAlumno):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "SELECT nombre, TIMESTAMPDIFF(YEAR, fechaNac, CURDATE()) AS edad FROM `curso` WHERE `curso`.`ID` = ?;"
                result = cursor.execute(sql, int(idAlumno))
                print(result)

            except Error as err:
                print("Error en la conexión", err)

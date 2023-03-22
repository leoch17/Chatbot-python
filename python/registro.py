import mysql.connector


class Historial:

    def __init__(self):
        self.cnn = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="chatbot")

    def insertar_historial_peticion(self, Peticion):
        cur = self.cnn.cursor()  # El cursor permite ejecutar la consulta cnn (conexion)
        sql = '''INSERT INTO historial (Peticion) VALUES ('{}')'''.format(
            Peticion)
        cur.execute(sql)  # El "cur.execute" permite ejecutar la variable "sql"
        n = cur.rowcount  # La variable "n" permite saber cuantas filas fueron actualizadas por la ejecución del cursor
        self.cnn.commit()  # Confirmar la accion que se esta ejecutando.
        cur.close()  # Finaliza la ejecución del cursor
        return n

    def insertar_historial_carpeta(self, Carpeta):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO historial (Carpeta) VALUES ('{}')'''.format(
            Carpeta)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()  # Confirmar la accion que se esta ejecutando.
        cur.close()
        return n

    def insertar_historial_documento(self, Documento):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO historial (Documento) VALUES ('{}')'''.format(
            Documento)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()  # Confirmar la accion que se esta ejecutando.
        cur.close()
        return n

import mysql.connector
from tabulate import tabulate


class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida a la base de datos")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def execute_stored_procedure(self, procedure_name):
        try:
            self.cursor.callproc(procedure_name)
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    print(tabulate(rows, headers=headers, tablefmt="pretty"))
                else:
                    print("No se encontraron resultados")
        except mysql.connector.Error as e:
            print(f"Error al ejecutar procedimiento almacenado: {e}")

    def execute_insert_procedure(self, procedure_name, *args):
        try:
            self.cursor.callproc(procedure_name, args)
            self.connection.commit()
            print("Datos insertados correctamente")
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"Error al insertar datos: {e}")

    def execute_update_procedure(self, procedure_name, *args):
        try:
            self.cursor.callproc(procedure_name, args)
            self.connection.commit()
            print("Datos actualizados correctamente")
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"Error al actualizar datos: {e}")


user = 'root'
password = ''
host = 'localhost'
database = 'sistema_de_gestion_de_clientes'

db_connector = DatabaseConnector(host, user, password, database)
db_connector.connect()

print("Mostrando detalles de todos los clientes:")
db_connector.execute_stored_procedure('clientes')

print("\nAgregando un cliente:")
db_connector.execute_update_procedure('AgregarCliente', 111, 'Isabel', 'isatares@gmail.com', 2707678)

print("\nMostrando detalles de todos los empleados después de la actualización:")
db_connector.execute_stored_procedure('clientes')

db_connector.disconnect()

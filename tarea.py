#archivo para conexion a base de datos
import pymysql

# Conexión a la base de datos
conn = pymysql.connect(host='localhost', user='root', passwd='', database='universidad', port=3306)

# Función para consultar modalidades
def consultar_modalidad():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM modalidad')
    resultado = cursor.fetchall()
    for fila in resultado:
        print(fila[1])

# Función para insertar una carrera
def insertar_carrera():
    cursor = conn.cursor()
    try:
        # Corrección en el comando SQL, era 'INSERT' en lugar de 'ISERT'
        cursor.execute("INSERT INTO carrera(codigo, nombre, id_modalidad) VALUES ('COMP_01', 'Juan', '1')")
        conn.commit()
        print("Carrera insertada exitosamente.")
    except pymysql.Error as e:
        print("Error al insertar la carrera:", e)

# Función para consultar carreras
def consultar_carrera():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera')
    resultado = cursor.fetchall()
    for fila in resultado:
        print(fila[0], ' - ', fila[1], ' - ', fila[2])

# Llamadas a las funciones
insertar_carrera()
consultar_carrera()

# Cerrar la conexión a la base de datos
conn.close()
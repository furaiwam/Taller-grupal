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
        
def seleccionar_todas_las_carreras():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carrera")
    return cursor.fetchall()

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

#  Actualizar el nombre de una carrera dado su código
def actualizar_nombre_carrera(codigo, nuevo_nombre):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE carrera
        SET nombre = ?
        WHERE codigo = ?
    ''', (nuevo_nombre, codigo))
    conn.commit()

# Eliminar una carrera dado su id
def eliminar_carrera_por_id(id_carrera):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carrera WHERE id = ?", (id_carrera,))
    conn.commit()

# Función para consultar carreras

def consultar_carrera():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera')
    resultado = cursor.fetchall()
    for fila in resultado:
        print(fila[0], ' - ', fila[1], ' - ', fila[2])

# Llamadas a las funciones
consultar_modalidad()
seleccionar_todas_las_carreras()
insertar_carrera()
actualizar_nombre_carrera()
eliminar_carrera_por_id()
consultar_carrera()

# Cerrar la conexión a la base de datos
conn.close()
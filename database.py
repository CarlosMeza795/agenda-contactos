import sqlite3

NOMBRE_DB = "contactos.db"

def conectar():
    conexion = sqlite3.connect(NOMBRE_DB)
    return conexion

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            email TEXT
        )
    """)

    conexion.commit()
    conexion.close()

def agregar_contacto(nombre, telefono, email):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO contactos (nombre, telefono, email)
        VALUES (?, ?, ?)
    """, (nombre, telefono, email))

    conexion.commit()
    conexion.close()

def listar_contactos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM contactos ORDER BY nombre")
    contactos = cursor.fetchall()

    conexion.close()
    return contactos

def buscar_contacto(nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM contactos
        WHERE nombre LIKE ?
    """, (f"%{nombre}%",))

    contactos = cursor.fetchall()
    conexion.close()
    return contactos

def eliminar_contacto(id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM contactos WHERE id = ?", (id,))

    conexion.commit()
    conexion.close()
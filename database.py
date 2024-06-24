import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL,
            categoria TEXT,
            proveedor TEXT,
            fecha_ingreso DATE,
            activo BOOLEAN NOT NULL DEFAULT 1
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_registro DATE,
            activo BOOLEAN NOT NULL DEFAULT 1,
            notas TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            email TEXT,
            fecha_contratacion DATE,
            puesto TEXT,
            salario REAL NOT NULL,
            activo BOOLEAN NOT NULL DEFAULT 1
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()

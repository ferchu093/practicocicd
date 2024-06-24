from database import get_db_connection

def create_producto(nombre, descripcion, precio, cantidad, categoria, proveedor, fecha_ingreso, activo):
    conn = get_db_connection()
    conn.execute('INSERT INTO producto (nombre, descripcion, precio, cantidad, categoria, proveedor, fecha_ingreso, activo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (nombre, descripcion, precio, cantidad, categoria, proveedor, fecha_ingreso, activo))
    conn.commit()
    conn.close()

def get_productos():
    conn = get_db_connection()
    productos = conn.execute('SELECT * FROM producto').fetchall()
    conn.close()
    return productos

def create_cliente(nombre, apellido, direccion, telefono, email, fecha_registro, activo, notas):
    conn = get_db_connection()
    conn.execute('INSERT INTO cliente (nombre, apellido, direccion, telefono, email, fecha_registro, activo, notas) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                 (nombre, apellido, direccion, telefono, email, fecha_registro, activo, notas))
    conn.commit()
    conn.close()

def get_clientes():
    conn = get_db_connection()
    clientes = conn.execute('SELECT * FROM cliente').fetchall()
    conn.close()
    return clientes

def create_empleado(nombre, apellido, direccion, telefono, email, fecha_contratacion, puesto, salario, activo):
    conn = get_db_connection()
    conn.execute('INSERT INTO empleado (nombre, apellido, direccion, telefono, email, fecha_contratacion, puesto, salario, activo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (nombre, apellido, direccion, telefono, email, fecha_contratacion, puesto, salario, activo))
    conn.commit()
    conn.close()

def get_empleados():
    conn = get_db_connection()
    empleados = conn.execute('SELECT * FROM empleado').fetchall()
    conn.close()
    return empleados

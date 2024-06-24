CREATE TABLE producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    categoria TEXT,
    proveedor TEXT,
    fecha_ingreso DATE,
    activo BOOLEAN NOT NULL DEFAULT 1
);
CREATE TABLE cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    email TEXT,
    fecha_registro DATE,
    activo BOOLEAN NOT NULL DEFAULT 1,
    notas TEXT
);
CREATE TABLE empleado (
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
);

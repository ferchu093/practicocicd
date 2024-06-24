from flask import Flask, render_template, request, redirect, url_for
from database import create_tables
import models

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        categoria = request.form['categoria']
        proveedor = request.form['proveedor']
        fecha_ingreso = request.form['fecha_ingreso']
        activo = request.form['activo']
        
        models.create_producto(nombre, descripcion, precio, cantidad, categoria, proveedor, fecha_ingreso, activo)
        return redirect(url_for('productos'))
    
    productos = models.get_productos()
    return render_template('productos.html', productos=productos)

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        fecha_registro = request.form['fecha_registro']
        activo = request.form['activo']
        notas = request.form['notas']
        
        models.create_cliente(nombre, apellido, direccion, telefono, email, fecha_registro, activo, notas)
        return redirect(url_for('clientes'))
    
    clientes = models.get_clientes()
    return render_template('clientes.html', clientes=clientes)

@app.route('/empleados', methods=['GET', 'POST'])
def empleados():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        fecha_contratacion = request.form['fecha_contratacion']
        puesto = request.form['puesto']
        salario = request.form['salario']
        activo = request.form['activo']
        
        models.create_empleado(nombre, apellido, direccion, telefono, email, fecha_contratacion, puesto, salario, activo)
        return redirect(url_for('empleados'))
    
    empleados = models.get_empleados()
    return render_template('empleados.html', empleados=empleados)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

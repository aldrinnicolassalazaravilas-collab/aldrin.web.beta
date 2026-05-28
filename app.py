from flask import Flask, request

app = Flask(__name__)




@app.route("/")
def inicio():
    return """
    <h1>Bienvenido a mi sitio web</h1>
    <p>Este es un sitio web de prueba</p>
    <a href="/saludo">Saludar</a><br>
    <a href="/informacion web">Información de la web</a><br>
    <a href="/almacen_de_datos">entrar al almacen de datos o conceptos pequeños</a><br>
    <form action="/saludo" method="get">
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        <button type="submit">Enviar</button>
    </form>
    """

@app.route("/almacen_de_datos")
def almacen_de_datos():
    return """
    <h1>Almacen de Datos</h1>
    <p>Esta es una página para almacenar datos.</p>
    <a href="/">Regresar a inicio</a><br>
    <a href="/que_es_python">¿que es python?</a><br>
    """
 
@app.route("/que_es_python") 
def que_es_python():
    return """
    <h1>¿que es python?</h1>
    <p>Python es un lenguaje de programación de alto nivel, interpretado, multipropósito y de código abierto..</p>
    <a href="/">Regresar a inicio</a><br>
    <a href="/almacen_de_datos">Regresar a almacen de datos</a><br>
    <a href="/python_conceptos_basicos">ver los conceptos basicos</a><br>

    """ 


@app.route("/saludo")
def saludo():
    # Intenta obtener el nombre de los parámetros de la URL
    nombre = request.args.get("nombre")
    if nombre:
        return f"<h1>Hola {nombre}, espero que disfrutes la web!</h1><a href='/'>Regresar a inicio</a>"
    return """<h1>Hola usuario espero que disfrutes la web!</h1>
        <a href="/">Regresar a inicio</a><br>
    """
    
@app.route("/informacion web")
def informacion_web():
    return """
    <h1>Información de la web</h1>
    <p>Esta es una web de prueba creada con Flask.</p>
    <p>la cual solo sirve para mostrar información de esta misma pagina web .</p>
    <a href="/">Regresar a inicio</a><br>
    <a href="/creador_de_la_web">informacion del creador de la web</a><br>
    """
   

@app.route("/creador_de_la_web")
def ver_codigo_web():
    return """
    <h1>creador de la web</h1>
    <p>El creador de esta pagina web es Aldrin Nicolas Salazar Avilas. creada solo para un bruebita.</p>
    <a href="/">Regresar a inicio</a><br>

    """
@app.route("/python_conceptos_basicos") 
def python_conceptos_basicos():
    return """
    <h1>conceptos basicos de python</h1>
    <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Conceptos de Python</title>
</head>
<body>

    <h1>Conceptos Básicos de Python</h1>

    <h2>1. print()</h2>
    <p>Sirve para mostrar mensajes en pantalla.</p>

    <pre>
print("Hola mundo")
    </pre>

    <hr>

    <h2>2. input()</h2>
    <p>Sirve para pedir datos al usuario.</p>

    <pre>
nombre = input("¿Cuál es tu nombre?")
    </pre>

    <hr>

    <h2>3. Variables</h2>
    <p>Las variables guardan información.</p>

    <pre>
edad = 14
nombre = "Aldrin"
    </pre>

    <hr>

    <h2>4. Tipos de datos</h2>

    <ul>
        <li>str = texto</li>
        <li>int = números enteros</li>
        <li>float = números decimales</li>
        <li>bool = verdadero o falso</li>
    </ul>

    <hr>

    <h2>5. Conversión de datos</h2>

    <pre>
numero = int(input("Dime un número"))
    </pre>

    <p>Convierte texto en número entero.</p>

    <hr>

    <h2>6. if</h2>

    <pre>
if nombre == "Aldrin":
    print("Bienvenido")
    </pre>

    <p>Sirve para tomar decisiones.</p>

    <hr>

    <h2>7. elif y else</h2>

    <pre>
if opcion == "1":
    print("Hola")

elif opcion == "2":
    print("Adiós")

else:
    print("Opción inválida")
    </pre>

    <hr>

    <h2>8. Operadores Matemáticos</h2>

    <ul>
        <li>+ suma</li>
        <li>- resta</li>
        <li>* multiplicación</li>
        <li>/ división</li>
    </ul>

    <hr>

    <h2>9. Funciones</h2>

    <pre>
def saludar():
    print("Hola")
    </pre>

    <p>Permiten reutilizar código.</p>

    <hr>

    <h2>10. return</h2>

    <pre>
def sumar():
    return 5 + 5
    </pre>

    <p>Devuelve un resultado.</p>

    <hr>

    <h2>11. while</h2>

    <pre>
while True:
    print("Hola")
    </pre>

    <p>Repite código varias veces.</p>

    <hr>

    <h2>12. Listas</h2>

    <pre>
historial = []
historial.append("Hola")
    </pre>

    <p>Guardan varios datos.</p>

    <hr>

    <h2>13. Importar módulos</h2>

    <pre>
import time
import datetime
    </pre>

    <p>Agregan funciones extras a Python.</p>

    <hr>

    <h2>14. Flask</h2>

    <pre>
from flask import Flask
app = Flask(__name__)
    </pre>

    <p>Sirve para crear páginas web con Python.</p>

    <hr>

    <h2>15. Rutas en Flask</h2>

    <pre>
@app.route("/")
def inicio():
    return "Hola"
    </pre>

    <p>Conectan URLs con funciones.</p>

</body>
</html>
    
    ""
   
    """
if __name__ == "__main__":
    
    # El modo debug permite ver cambios en tiempo real sin reiniciar manualmente
    print("Iniciando servidor en http://127.0.0.1:5000")
    app.run(debug=True)
from flask import Flask, request
import datetime
import time
print(time  .ctime())



app = Flask(__name__)
mensaje = ""



@app.route("/")
def inicio():
    return """
    <h1>Bienvenido a mi sitio web</h1>

    <p>Este es un sitio web de prueba</p>

    <p><a href="/saludo">Saludar</a></p>

    <p><a href="/informacion_web">Información de la web</a></p>

    <p><a href="/almacen_de_datos">
    Entrar al almacén de datos o conceptos pequeños
    </a></p>

    <p><a href="/apps_disponibles">
    Apps disponibles desde mi web
    </a></p>

    <form action="/saludo" method="get">
        <input type="text" name="nombre" placeholder="Escribe tu nombre">
        <button type="submit">Enviar</button>
    </form>

    <p><a href="/mensaje_intercontinental">
    Enviar un mensaje intercontinental
    </a></p>

    <p><a href="/reloj">
    Ver la hora actual
    </a></p>

    <p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSfZQYISApXiOVRlwpHlv_xBrzprV4QS7W6nZbosH8W38arQmQ/viewform?usp=dialog" target="_blank">
            Realiza esta encuesta que es de un proyecto de mi escula porfa
        </a>
    </p>

    <style>
      body{
        font-size: 20px;
        background-color: white;
      }

      input{
        font-size: 19px;
      }

      button{
        font-size: 19px;
      }
    </style>
    """
    
@app.route("/almacen_de_datos")
def almacen_de_datos():
    return """
    <h1>Almacen de Datos</h1>
    <p>Esta es una página para almacenar datos.</p>
    <a href="/">Regresar a inicio</a><br>
    <a href="/que_es_python">¿que es python?</a><br>
    <style>
      body{
        font-size: 20px; ;
        }
        </style>
    """
 
@app.route("/que_es_python") 
def que_es_python():
    return """
    <h1>¿que es python?</h1>
    <p>Python es un lenguaje de programación de alto nivel, interpretado, multipropósito y de código abierto..</p>
    <a href="/">Regresar a inicio</a><br>
    <a href="/almacen_de_datos">Regresar a almacen de datos</a><br>
    <a href="/python_conceptos_basicos">ver los conceptos basicos</a><br>
    <style>
      body{
        font-size: 20px; ;
        }
        body{
        background-color:#FFE599;                                                                                                     
        }
        </style>

    """ 


@app.route("/saludo")
def saludo():
    # Intenta obtener el nombre de los parámetros de la URL
    nombre = request.args.get("nombre")
    if nombre:
        return f"<h1>Hola {nombre}, espero que disfrutes la web!</h1><a href='/'>Regresar a inicio</a>"
    return """<h1>Hola usuario espero que disfrutes la web!</h1>
        <a href="/">Regresar a inicio</a><br>
         body{
         <style>
        font-size: 20px; ;
        }

    """
    
@app.route("/informacion_web")
def informacion_web():
    return """
    <h1>Información de la web</h1>
    <p>Esta es una web de prueba creada con Flask.</p>
    <p>la cual solo sirve para mostrar información de esta misma pagina web .</p>
    <a href="/">Regresar a inicio</a><br>
    <a href="/creador_de_la_web">informacion del creador de la web</a><br>
        
        <style>
        font-size: 50px; ;
        }
        </style>

    """
   

@app.route("/creador_de_la_web")
def ver_codigo_web():
    return """
    <h1>creador de la web</h1>
    <p>El creador de esta pagina web es Aldrin Nicolas Salazar Avilas. creada solo para un bruebita.</p>
    <a href="/">Regresar a inicio</a><br>
        <style>
        font-size: 50px; ;
        }
        </style>
      


    """
@app.route("/apps_disponibles")
def apps(): 
  return """
  <a href="https://chatgpt.com" target="_blank">
        
          
          <h4>Entrar a ChatGPT</h4>
          """
historial = []

@app.route("/mensaje_intercontinental", methods=["GET", "POST"])
def mensaje_intercontinental():

    if request.method == "POST":

        mensaje = request.form["mensaje"]
        historial.append(mensaje)

        print(mensaje)

    mensajes_html = ""

    for m in historial:
        mensajes_html += f"<p>{m}</p>"

    return f"""

    <h1>Mensaje Intercontinental</h1>

    <form method="POST">

        <input type="text" name="mensaje" placeholder="Escribe tu mensaje">

        <button type="submit">Enviar</button>

    </form>

    <h2>Historial:</h2>

    {mensajes_html}

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
    <a href="/">Regresar a inicio</a><br>
    <a href="/que_es_python">¿que es python?</a><br>
</body>
</html>
    
  
...
<style>
body{
    font-size: 20px;
    background-color:#FFD966;
}
</style>
"""

@app.route("/reloj")
def reloj():
    return """
    <h1>Reloj en vivo</h1>

    <h2 id="hora">Cargando...</h2>

    <script>
    function actualizarHora() {
        let ahora = new Date()
        document.getElementById("hora").innerText = ahora.toLocaleTimeString()
    }

    setInterval(actualizarHora, 1000)
    actualizarHora()
    </script>

    <a href="/">Regresar al inicio</a>
    """

   
     


    
if __name__ == "__main__":
    print("Iniciando servidor")
    app.run(debug=True)
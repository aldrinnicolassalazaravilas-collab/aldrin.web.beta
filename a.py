from flask import Flask, request

app = Flask(__name__)

usuarios = ["Aldrin 777", "maicol 67", "maria 1234"]

@app.route("/", methods=["GET", "POST"])
def inicio():

    mensaje = ""

    if request.method == "POST":

        nombre = request.form.get("nombre")

        if nombre in usuarios:

            mensaje = f" Bienvenido {nombre}"

        else:

            crear = request.form.get("crear")

            if crear == "si":

                usuarios.append(nombre)

                mensaje = " Cuenta creada exitosamente"

            else:

                mensaje = "No encontramos tu cuenta"

    return f"""
    <!DOCTYPE html>

    <html lang="es">

    <head>

        <meta charset="UTF-8">

        <title>Sistema de Usuarios</title>

        <style>

            body{{
                background:#1e1e1e;
                color:white;
                font-family:Arial;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }}

            .caja{{
                background:#2d2d2d;
                padding:30px;
                border-radius:15px;
                text-align:center;
                width:350px;
            }}

            input{{
                width:90%;
                padding:10px;
                margin:10px;
                border:none;
                border-radius:10px;
            }}

            button{{
                padding:10px 20px;
                border:none;
                border-radius:10px;
                cursor:pointer;
                margin:5px;
                background:green;
                color:white;
                font-size:16px;
            }}

            h2{{
                margin-top:20px;
            }}

        </style>

    </head>

    <body>

        <div class="caja">

            <h1>Sistema de Usuarios</h1>

            <form method="POST">

                <input 
                    type="text" 
                    name="nombre" 
                    placeholder="Ingresa tu usuario"
                    required
                >

                <br>

                <button type="submit">
                    Entrar
                </button>

                <button 
                    type="submit"
                    name="crear"
                    value="si"
                >
                    Crear Cuenta
                </button>

            </form>

            <h2>{mensaje}</h2>

        </div>

    </body>

    </html>
    """

app.run(debug=True)



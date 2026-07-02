from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def inicio(): 
#main#
 return render_template("AI del programa/asistente_ai.html")






#seccion de juegos#

@app.route("/Partes del computador")
def partes_del_computador_1():
      return render_template("juegos/buscar_partes_de_computer.html")




@app.route("/robot_controler")
def robot_controller():
   return render_template("juegos/robot_controler.html")
   
#seccion de Guias#




if __name__ == "__main__":
   print("Iniciando servidor")
   app.run(debug=True)
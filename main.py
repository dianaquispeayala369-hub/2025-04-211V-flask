from flask import Flask, render_template, request

app = Flask(__name__)


base_de_datos = ["jorge","pepe","juanito"] #Modelos

@app.route("/") # controlador
def hello():
    return render_template(template_name_or_list="index.html", datos= base_de_datos) #visualizacion o view
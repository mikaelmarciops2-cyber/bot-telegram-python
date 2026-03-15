from triagem import classificar
from flask import Flask, render_template, request

app = Flask(__name__)
fila = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/data', methods=['POST'])
def receive_data():

    nome = request.form["nome"]
    dor = int(request.form['dor'])
    temperatura = float(request.form["temperatura"])

    resultado = classificar(temperatura, dor)

    fila.append({
        "nome": nome,
        "prioridade": resultado
    })

    return f"Paciente {nome} classificado como {resultado}"

app.run(debug=True)

@app.route("/fila")
def ver_fila():
    return str(fila)
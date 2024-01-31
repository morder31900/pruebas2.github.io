from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar_edad', methods=['POST'])
def verificar_edad():
    edad_str = request.form['edad']
    edad = int(edad_str)

    if edad >= 18:
        mensaje = "Es mayor de edad."
    else:
        mensaje = "No es mayor de edad."

    return render_template('resultado.html', mensaje=mensaje, edad=edad)

if __name__ == '__main__':
    app.run(debug=True)

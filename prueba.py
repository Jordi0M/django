
from flask import Flask, session, request
import random

app = Flask(__name__)
app.secret_key = 'h'


@app.route("/")
def hello():

    return """
    <form action="login" method="POST">
    	<p>Introduc un numero del 1 al 10:</p>
    	<input type=text name=numero_usuario>
    	<input type=submit>
    </form>

    """




@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'random' in session:
        print(session['random'])
    else:
        rand = random.randrange(1,11,1) #del 1 al 10 de uno en uno
        session['random'] = rand

    if request.method == 'POST':
    	numero_usuario = request.form['numero_usuario']
    	print(numero_usuario)
    	

    	if int(numero_usuario) > session['random']:
    		return "el numero introducido es mayor al que tienes que adivinar"
    	elif int(numero_usuario) < session['random']:
    		return "el numero introducido es menor al que tienes que adivinar"
    	elif int(numero_usuario) == session['random']:
    		return "adivinaste"
    else:
        return "recibido por POST"
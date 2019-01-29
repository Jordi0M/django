
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():

    return """
    <form action="login" method="POST">
    	<p>Introduc un numero del 1 al 10:</p>
    	<input type=text name=numero_usuario>
    	<input type=submit>
    </form>

    """

import random
rand = random.randrange(1,11,1) #del 1 al 10 de uno en uno


from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    	numero_usuario = request.form['numero_usuario']
    	print(numero_usuario)
    	

    	if int(numero_usuario) > rand:
    		return "el numero introducido es mayor al que tienes que adivinar"
    	elif int(numero_usuario) < rand:
    		return "el numero introducido es menor al que tienes que adivinar"
    	elif int(numero_usuario) == rand:
    		return "adivinaste"
    else:
        return "recibido por POST"
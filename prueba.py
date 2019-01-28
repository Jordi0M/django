# apt install python3-pip
#pip3 install virtualenv
#virtualenv envlFlask
#pip3 freeze
#source envFlask/bin/activate
#pip3 freeze
#pip install flask
#pip3 freeze

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():

    return """
    <form action="login">
    	<p>Introduc un numero del 1 al 10:</p>
    	<input type=text name=numero_usuario>
    	<input type=submit>
    </form>

    """

import random
rand = random.randrange(0,11,1) #del 0 al 10 de uno en uno


from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
    	numero_usuario = request.args.get('numero_usuario')

    	if int(numero_usuario) > rand:
    		return "el numero es mayor al que tienes que adivinar"
    	elif int(numero_usuario) < rand:
    		return "el numero es menor al que tienes que adivinar"
    	elif int(numero_usuario) == rand:
    		return "adivinaste"
    else:
        return "recibido por POST"
from flask import Flask, render_template
from random import randint



app = Flask(__name__)


@app.route('/test', methods=['GET'])
def hello():
    dizionario = {'x': randint(0, 100), 
                 'y': randint(100, 300)}
    return render_template('index.html', dizionario=dizionario)
    
    
@app.route('/fff')
def ff():
    return Response('hello world', 'text/plain')    


app.run(host="0.0.0.0", port=80)



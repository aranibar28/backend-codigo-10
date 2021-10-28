import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola a todos, esto una prueba de despliegue con Heroku'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
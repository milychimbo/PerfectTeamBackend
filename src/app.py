from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, bienvenido al backend de Perfect Team!"
    

if __name__ == '__main__':
    app.run()
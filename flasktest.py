from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "hello this is the home page <h1>HELLO<h1>"


@app.route("/<name>")
def user(name):
    return f'Hello {name}' 

if __name__ == '__main__':
    app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/')
def land():
    return {
        "Im getting the hang of this" : "Super comfy"
    }

@app.route('/home')
def home():
    return {
        "Im getting the hang of this" : "Super comfy"
    }

@app.route('/students')
def student():
    return {
        "Im getting the hang of this" : "Super comfy"
    }

@app.route('/test')
def test():
    return {
        "Im getting the hang of this" : "Super comfy"
    }

app.run()
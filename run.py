from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def land():
    return {
        "Im getting the hang of this" : "Super comfy"
    }



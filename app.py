from flask import Flask

app = Flask(__name__)

@app.route('/')
def halo():
    return "Halo World Rama Testing"
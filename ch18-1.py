from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

app.run(host='172.26.210.174')
app.run(port=8000)
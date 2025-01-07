from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info/ceo')
def ceo():
    return render_template("info/ceo.html")

app.run(port=80, debug=True)

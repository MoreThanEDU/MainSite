from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/')
def companyinfo():
    return render_template(".html")

app.run(port=80, debug=True)

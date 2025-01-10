from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info/ceo')
def ceo():
    return render_template("info/ceo.html")

@app.route('/info/vision')
def vision():
    return render_template("info/vision.html")

@app.route('/info/organization')
def organization():
    return render_template("info/organization.html")

@app.route('/buis/Attendify')
def Attendify():
    return render_template("buis/Attendify.html")

@app.route('/promotions')
def promotions():
    return '<script>alert("프로모션 준비중입니다.");history.back();</script>'

@app.route('/customer/notice')
def notice():
    return render_template("customer/notice.html")

@app.route('/customer/qna')
def qna():
    return render_template("customer/qna.html")

@app.route('/customer/inquiry')
def inquiry():
    return render_template("customer/inquiry.html")

@app.route('/menus')
def menus():
    return render_template("menus.html")

app.run(port=80, debug=True)

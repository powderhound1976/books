from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/browse")
def browse():
    return render_template("browse.html")


@app.route("/art")
def art():
    return render_template("art.html")


@app.route("/biography")
def biography():
    return render_template("biography.html")


@app.route("/business")
def business():
    return render_template("business.html")


@app.route("/book1")
def book1():
    return render_template("book1.html")


@app.route("/book2")
def book2():
    return render_template("book2.html")


@app.route("/book3")
def book3():
    return render_template("book3.html")


@app.route("/book4")
def book4():
    return render_template("book4.html")


@app.route("/book5")
def book5():
    return render_template("book5.html")


@app.route("/book6")
def book6():
    return render_template("book6.html")


@app.route("/book7")
def book7():
    return render_template("book7.html")


@app.route("/book8")
def book8():
    return render_template("book8.html")


@app.route("/book9")
def book9():
    return render_template("book9.html")

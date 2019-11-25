from flask import Flask,render_template

app = Flask(__name__)


@app.route('/a9')
def a9():
    return render_template("a9.html")



@app.route('/a8')
def a8():
    return render_template("a8.html")



@app.route('/a7')
def a7():
    return render_template("a7.html")


@app.route('/a6')
def a6():
    return render_template("a6.html")



@app.route('/a5')
def a5():
    return render_template("a5.html")



@app.route('/a4')
def a4():
    return render_template("a4.html")

@app.route('/a3')
def a3():
    return render_template("a3.html")



@app.route('/a2')
def a2():
    return render_template("a2.html")

@app.route('/a1')
def a1():
    return render_template("a1.html")

@app.route('/')
def login():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

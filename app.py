from flask import Flask
from flask import render_template
from flask import request

# webアプリを作る
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "やっほーー 平泉町"


@app.route("/user/<name>")
def heyName(name):
    return name


@app.route("/user/<name>/<age>")
def heyAge(name, age):
    return "私は" + name + "、" + str(age) + "歳"


# from flask import render_template
@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/name/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


# @app.route("/html/<aaa>")
# def htmlnamae(aaa):
#     return render_template("ma,e.html", name=aaa)


@app.route("/html/age/<age>")
def age(age):
    return render_template("age.html", htmlAge=age)


@app.route("/query")  # なぜエラー線でているのか -> 何も入っていないもの(NULLのもの)を返す可能性があることを知らせているだけ
def query():
    search_text = request.args.get("search_text")
    if search_text is not None:
        return search_text
    else:
        return "NONE"


# http://127.0.0.1:5000/query?search_text=AAA

# @app.route("/query")
# def query():
#     BBB = request.args.get("AAA")
#     return BBB
# http://127.0.0.1:5000/query?AAA=XXX


# 起動する
# app.run(port=5001)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/")
def homepage():
    return render_template("index.html", h1="NO")


@app.route("/docs")
def docs():
    return render_template("docs.html", title="docs page")


@app.route("/about")
def about():
    return render_template("about.html", title="about page")


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template

application = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@application.route("/")
def homepage():
    return render_template("index.html", h1="NO")


@application.route("/docs")
def docs():
    return render_template("docs.html", title="docs page")


@application.route("/about")
def about():
    return render_template("about.html", title="about page")


if __name__ == "__main__":
    application.run()

from flask import Flask, render_template

class app:

    app = Flask(__name__)


@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index_html")

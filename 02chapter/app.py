from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def render_main():
    return render_template("index.html")


# set up Flask to listen to the port
app.run('localhost', 8000, debug=True)

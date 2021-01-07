from flask import Flask, render_template

app = Flask(__name__)


@app.route('/departures/')
@app.route('/departures/<departure>/')
def render_departures(departure='Limpopo'):
    return f'Departures page\nMain departure of all times: {departure}'


@app.route('/tours/<int:id>')
def render_tours():
    return 'Tours page'


#  request to '/' results in render_main() run
@app.route('/')
def render_main():
    # return render_template("main.html")
    return 'Main page'


def main():
    app.run('localhost', 8000)


if __name__ == '__main__':
    main()



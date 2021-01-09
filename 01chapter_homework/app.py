from flask import Flask, render_template

app = Flask(__name__)


@app.route('/departures/')
@app.route('/departures/<departure>/')
def render_departures(departure='Limpopo'):
    return render_template("departure.html")


@app.route('/tours/')
@app.route('/tours/<int:tour_id>')
def render_tours(tour_id=0):
    return render_template("tour.html")


@app.route('/')
def render_main():
    return render_template("index.html")


def main():
    app.run('localhost', 8000)


if __name__ == '__main__':
    main()



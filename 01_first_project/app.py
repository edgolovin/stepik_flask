from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/<departure>/')
def render_departures(departure):
    if departure in data.departures.keys():
        return render_template("departure.html", departure=departure)
    else:
        return render_template("no_departure.html")


@app.route('/tours/<int:tour_id>')
def render_tours(tour_id):
    return render_template("tour.html", tour_id=tour_id)


@app.route('/')
@app.route('/tours/')
@app.route('/departures/')
def render_index():
    return render_template("index.html")


@app.context_processor
def inject_data():
    return dict(data=data)


def main():
    app.run('localhost', 8000, debug=True)


if __name__ == '__main__':
    main()



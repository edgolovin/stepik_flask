from flask import Flask, render_template
import data

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
def render_index():
    return render_template("index.html")


def make_tour_short_description(k):
    country = data.tours[k]['country'] + ':'
    href = f'<a href="/data/tours/{k}">'
    title = data.tours[k]['title']
    price = data.tours[k]['price']
    stars = data.tours[k]['stars'] + '*'
    return f'<p>{country} {href}{title} {price} {stars}</a></p>\n'


@app.route('/data/')
def render_data():
    raw_html = '<h1>Все туры</h1>\n\n'
    for k in data.tours.keys():
        raw_html += make_tour_short_description(k)
    return raw_html


@app.route('/data/departures/')
@app.route('/data/departures/<dep_id>')
def render_data_departures(dep_id=''):
    if not dep_id:
        return render_data()
    elif dep_id in data.departures.keys():
        raw_html = f'<h1>Туры по направлению {data.departures[dep_id]}</h1>\n\n'
        for i in range(1, 17):
            if dep_id == data.tours[i]['departure']:
                raw_html += make_tour_short_description(i)
        return raw_html
    else:
        return 'There\'s no departure from this city'


def make_tour_full_description(tour_id):
    tour = data.tours[tour_id]
    raw_html = f'<h1>{tour["country"]}: {tour["title"]} {tour["price"]}:</h1>\n\n'
    raw_html += f'<p>{tour["nights"]} ночей</p>'
    raw_html += f'<p>Стоимость: {tour["price"]} Р</p>'
    raw_html += f'<p>{tour["description"]}</p>'
    return raw_html


@app.route('/data/tours/')
@app.route('/data/tours/<int:tour_id>')
def render_tour(tour_id=0):
    if 0 < tour_id < 17:
        return make_tour_full_description(tour_id)
    else:
        return 'there are 16 tours'


def main():
    app.run('localhost', 8000, debug=True)


if __name__ == '__main__':
    main()



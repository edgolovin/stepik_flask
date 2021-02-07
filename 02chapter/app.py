from flask import Flask, render_template

app = Flask(__name__)

menu_links = [{'title': 'Главная', 'link': 'index'},
              {'title': 'Неглавная', 'link': 'not-main'},
              {'title': 'Third menu item', 'link': 'thirdlink'}]


@app.route('/')
@app.route('/index/')
def render_main():
    return render_template("index.html")


@app.route('/not-main/')
def render_secondary():
    return render_template("not-main.html")


@app.context_processor
def inject_menu_dict():
    return dict(menu_links=menu_links)


# set up Flask to listen to the port
app.run('localhost', 8000, debug=True)

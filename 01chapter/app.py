from flask import Flask, render_template

app = Flask(__name__)


@app.route('/products/')
@app.route('/products/<product_id>/')
@app.route('/products/<int:product_id>/<product_price>')
def render_products(product_id=0, product_price='unknown'):
    if product_id:
        return f'Here it is the product _{product_id}_ page. It\'s price is _{product_price}_'
    else:
        return 'Enter product id'


@app.route('/about/')
def render_about():
    return render_template('about.html', adj='shiny', noun='国家')


# render vars, list, dict in template
@app.route('/vars/')
def render_vars():
    return render_template('vars.html',
                           some_var='小猪佩奇',
                           rgb=['red', 'green', 'blue'],
                           capitals={'China': 'Beijing',
                                     'Paraguay': 'Asunción',
                                     'Indonesia': 'Jakarta'})


@app.route('/static-files')
def render_page_w_static_files():
    return render_template('static-files.html')


#  request to '/' results in render_main() run
@app.route('/')
def render_main():
    print('this text goes to console')
    return render_template("main.html")


# set up Flask to listen to the port
app.run('localhost', 8000)

from flask import Flask

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
    return 'About the project'


#  request to '/' results in hello() run
@app.route('/')
def render_main():
    print('this text goes to console')
    return 'Science, bitch!'


# set up Flask to listen to the port
app.run('localhost', 8000)

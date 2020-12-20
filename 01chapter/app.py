from flask import Flask

app = Flask(__name__)


#  request to '/' results in hello() run
@app.route('/')
def hello():
    print('fuck')
    return 'Science, bitch!'


# set up Flask to listen to the port
app.run('localhost', 8000)

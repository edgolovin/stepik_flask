from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/any_route_for_form/')
def render_login():
    form = """
    <form action="/any_name/" method="post">
      <input type="text" name="username">
      <input type="password" name="password">
      <input type="submit">
    </form>
    """
    return form


@app.route('/any_name/', methods=['POST'])
def render_search():
    username = request.form.get('username')
    password = request.form.get('password')
    return f'Логин: {username}; Пароль {password}'


def main():
    app.run('localhost', 8000, debug=True)


if __name__ == '__main__':
    main()

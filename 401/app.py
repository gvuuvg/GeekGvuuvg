import flask

app = flask.Flask(__name__, static_url_path='')


@app.route("/")
def home():
    return 'hello'


@app.route("/h")
def hom():
    return 'wrold'


@app.route("/a/<int:name>")
def dy(name):
    return 'wrold%s' % name


if __name__ == '__main__':
    print(app.url_map)
    app.run()

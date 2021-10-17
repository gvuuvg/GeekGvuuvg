import flask

app = flask.Flask(__name__)


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
    app.run()

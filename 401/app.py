import flask

app = flask.Flask(__name__, static_url_path='')





@app.route("/")
def home():
    return '''<form url="/info" method="post">"
        用户名：<input type="text">
        密码:<input type="text">
        <button>
            提交
        </button>
    </form>'''


@app.route("/a/<int:name>")
def dy(name):
    return 'wrold%s' % name

@app.route("/info",methods=["post"])
def info():
    return '登陆成功'


if __name__ == '__main__':
    print(app.url_map)
    app.run()

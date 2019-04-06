from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hellow world'

@app.route('/test')
def test():
    return '你好牛逼'

if __name__ == '__main__':
    app.run()

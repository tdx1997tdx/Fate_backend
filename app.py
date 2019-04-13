from flask import Flask,request
from flask import Flask,Request,request,render_template,redirect,url_for,session
from Servant_search import page2
app = Flask(__name__)
app.register_blueprint(page2)
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'hellow world'

@app.route('/test',methods=['GET','POST'])
def test():
    if(request.data=="我好牛逼"):
        return '你好牛逼'
    return '你不牛逼'

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

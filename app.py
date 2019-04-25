from flask import Flask,request
from route.Servant_search import page2
from route.Characteristics_search import page3
from route.Servent_information import page4
app = Flask(__name__)
app.register_blueprint(page2)
app.register_blueprint(page3)
app.register_blueprint(page4)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return '欢迎来到数据库期末Fate_project'


if __name__ == '__main__':
    app.run()

from flask import Flask
from route.Name_search import page2
from route.Characteristics_search import page3
from route.Servent_information import page4
from route.Explorer_infomation import page5
from route.Other_search import page6
app = Flask(__name__)
app.register_blueprint(page2)
app.register_blueprint(page3)
app.register_blueprint(page4)
app.register_blueprint(page5)
app.register_blueprint(page6)
app.config['JSON_AS_ASCII'] = True

@app.route('/',methods=['GET','POST'])
def hello_world():
    return '欢迎来到数据库期末Fate_project'


if __name__ == '__main__':
    app.run()

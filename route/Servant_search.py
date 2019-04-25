from flask import Blueprint, json,request
from op_sql import name_search_sql as nss
page2=Blueprint("page2",__name__)

@page2.route('/name_search',methods=['GET','POST'])
def name_search():
    print(request.form)
    print(request.data.decode('utf-8'))
    data = json.loads(request.data.decode('utf-8'))
    try:
        name=data['name']
    except:
        return 'Json Format Error'
    print(data)
    return json.jsonify(nss.name_search(name))


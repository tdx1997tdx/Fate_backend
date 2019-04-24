from flask import Blueprint, json,request
from op_sql import name_search_sql as nss
page2=Blueprint("page2",__name__)

@page2.route('/name_search',methods=['GET','POST'])
def name_search():
    data = json.loads(request.get_data())
    name=data.get('name')
    print(data)
    return json.jsonify(nss.name_search(name))


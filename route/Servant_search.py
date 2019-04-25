from flask import Blueprint, json,request
from op_sql import name_search_sql as nss
page2=Blueprint("page2",__name__)

@page2.route('/name_search',methods=['GET','POST'])
def name_search():
    try:
        data = json.loads(request.data)
    except:
        return 'No Json Input'
    try:
        name=data['name']
    except:
        return 'Json Format Error'
    print(data)
    return json.jsonify(nss.name_search(name))


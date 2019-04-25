from flask import Blueprint, json,request
from op_sql import servent_infomation_sql as sis
page4=Blueprint("page4",__name__)

@page4.route('/servent_infomation',methods=['GET','POST'])
def name_search():
    try:
        data = json.loads(request.get_data())
    except:
        return 'No Json Input'
    try:
        id=data['servent_id']
    except:
        return 'Json Format Error'
    print(data)
    return json.jsonify(sis.servent_infomation(id))
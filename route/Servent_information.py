from flask import Blueprint, json,request
from op_sql import servent_infomation_sql as sis
page4=Blueprint("page4",__name__)

@page4.route('/servent_infomation',methods=['GET','POST'])
def name_search():
    data = json.loads(request.get_data())
    id=data.get('servent_id')
    print(data)
    return json.jsonify(sis.servent_infomation(id))
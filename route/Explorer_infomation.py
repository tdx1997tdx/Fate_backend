from flask import Blueprint, json,request
from op_sql import explorer_infomation_sql as eis
page5=Blueprint("page5",__name__)

@page5.route('/explorer_infomation',methods=['GET','POST'])
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
    return json.jsonify(eis.explorer_infomation(id))
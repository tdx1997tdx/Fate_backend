from flask import Blueprint, json,request
from op_sql import characteristic_search_sql as css
import sys
page3=Blueprint("page3",__name__)

@page3.route('/characteristics_search',methods=['GET','POST'])
def name_search():
    try:
        data = json.loads(request.get_data())
    except:
        return 'No Json Input'
    info={}
    try:
        info['origin_name']=data['origin']
        info['region_name']=data['region']
        info['class_name']=data['class']
        info['alignment_name']=data['alignment']
    except:
        return 'Json Format Error'
    try:
        weight = []
        weight.append(0 if data.get('weight')[0]=='-1' else int(data.get('weight')[0]))
        weight.append(sys.maxsize if data.get('weight')[1] == '-1' else int(data.get('weight')[1]))
        height = []
        height.append(0 if data.get('height')[0] == '-1' else int(data.get('height')[0]))
        height.append(sys.maxsize if data.get('height')[1] == '-1' else int(data.get('height')[1]))
    except:
        return 'Weight Or Height Format Error'
    print(data)
    return json.jsonify(css.characteristic_search(info,weight,height))


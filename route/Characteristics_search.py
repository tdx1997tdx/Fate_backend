from flask import Blueprint, json,request
from op_sql import characteristic_search_sql as css
import sys
page3=Blueprint("page3",__name__)

@page3.route('/characteristics_search',methods=['GET','POST'])
def characteristics_search():
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
        weight.append(0 if data['weight_down']=='-1' else int(data['weight_down']))
        weight.append(10000 if data['weight_up'] == '-1' else int(data['weight_up']))
        height = []
        height.append(0 if data['height_down'] == '-1' else int(data['height_down']))
        height.append(10000 if data['height_up'] == '-1' else int(data['height_up']))
    except:
        return 'Weight Or Height Format Error'
    print(data)
    return json.jsonify(css.characteristic_search(info,weight,height))

@page3.route('/get_attribute',methods=['GET','POST'])
def get_attribute():
    return json.jsonify(css.get_attribute())

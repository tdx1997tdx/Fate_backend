from flask import Blueprint, json,request
from op_sql import other_search_sql as oss
page6=Blueprint("page6",__name__)

@page6.route('/prototype_search',methods=['GET','POST'])
def prototype_search():
    try:
        data = json.loads(request.get_data())
    except:
        return 'No Json Input'
    try:
        prototype=data['prototype']
    except:
        return 'Json Format Error'
    print(data)
    return json.jsonify(oss.prototype_search(prototype))

@page6.route('/region_search',methods=['GET','POST'])
def region_search():
    try:
        data = json.loads(request.get_data())
    except:
        return 'No Json Input'
    try:
        region=data['region']
    except:
        return 'Json Format Error'
    print(data)
    return json.jsonify(oss.region_search(region))

@page6.route('/origin_search',methods=['GET','POST'])
def origin_search():
    try:
        data = json.loads(request.get_data())
    except:
        return 'No Json Input'
    try:
        origin=data['origin']
    except:
        return 'Json Format Error'
    print(data)
    return json.jsonify(oss.origin_search(origin))
from basic_sql_op import op_database as opsql

'''
按姓名查询相关英灵
input: 英灵姓名
output: 按照json格式返回英灵的id,servent_name,servent_profile_pic属性。
'''
def name_search(name):
    db = opsql.Database()
    search_name = "%"
    for i in name:
        search_name += i
        search_name += "%"
    sql="select servent_id,servent_name from servent where servent_name like %s;"
    result = db.select(sql,[search_name])
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"]=row[1]
        temp_sql="select profile_pic from servent_profile_pic where servent_id= %s;"
        re=[i[0] for i in db.select(temp_sql,[row[0]])]
        dic_one_person_info["servent_profile_pic"] = re[0]
        dic_info.append(dic_one_person_info)
    db.close()
    return dic_info

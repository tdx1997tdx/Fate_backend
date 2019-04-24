from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
def name_search(name,conn_info=c.conn1_info):
    search_name = '%'
    for i in name:
        search_name += i
        search_name += '%'
    sql="select servent_id,servent_name from servent where servent_name like '%s'" % (search_name)
    result = [i for i in opsql.select(sql,conn_info)]
    dic_info = {}  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_info[row[0]] = dic_one_person_info
        dic_one_person_info["servent_name"]=row[1]
        temp_sql="select profile_pic from servent_profile_pic where servent_id='%s'" % (row[0])
        dic_one_person_info["servent_profile_pic"] = [i[0] for i in opsql.select(temp_sql,conn_info)]
    return dic_info

#print(name_search("兰陵王",c.conn2_info))
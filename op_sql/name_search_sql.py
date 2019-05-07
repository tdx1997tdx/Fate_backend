from basic_sql_op import op_postgresql as opsql
import basic_sql_op.conn_sql as c
def name_search(name,conn_info=c.get_now_conn()):
    search_name = '%'
    for i in name:
        search_name += i
        search_name += '%'
    sql="select servent_id,servent_name from servent where servent_name like '%s'"
    result = [i for i in opsql.select(sql,(search_name),conn_info)]
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"]=row[1]
        temp_sql="select profile_pic from servent_profile_pic where servent_id='%s'"
        re=[i[0] for i in opsql.select(temp_sql,(row[0]),conn_info)]
        dic_one_person_info["servent_profile_pic"] = re[0]
        dic_info.append(dic_one_person_info)
    return dic_info

#print(name_search("兰陵王",c.conn2_info))
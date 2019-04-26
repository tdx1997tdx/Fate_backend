from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
import random
def prototype_search(prototype,conn_info=c.get_now_conn()):
    sql = "select prototype_name,s.servent_id,servent_name,profile_pic from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype p on sp.prototype_id=p.prototype_id inner join servent_profile_pic spp on s.servent_id = spp.servent_id where prototype_name='%s'" % (prototype)
    result = [i for i in opsql.select(sql, conn_info)]
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"] = row[1]
        dic_one_person_info["servent_profile_pic"] = row[2]
        dic_info.append(dic_one_person_info)
    return dic_info

#print(name_search("兰陵王",c.conn2_info))
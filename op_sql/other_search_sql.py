from basic_sql_op import op_postgresql as opsql
import basic_sql_op.conn_sql as c


def prototype_search(prototype,conn_info=c.get_now_conn()):
    search = '%'
    for i in prototype:
        search += i
        search += '%'
    sql = "select s.servent_id,servent_name,profile_pic from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype p on sp.prototype_id=p.prototype_id inner join servent_profile_pic spp on s.servent_id = spp.servent_id where prototype_name like '%s'" % (search)
    result = [i for i in opsql.select(sql, conn_info)]
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"] = row[1]
        dic_one_person_info["servent_profile_pic"] = row[2]
        dic_info.append(dic_one_person_info)
    return dic_info

def region_search(region,conn_info=c.get_now_conn()):
    search= '%'
    for i in region:
        search += i
        search += '%'
    sql = "select s.servent_id,servent_name,profile_pic from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype p on sp.prototype_id=p.prototype_id inner join servent_profile_pic spp on s.servent_id = spp.servent_id inner join prototype_region pr on p.prototype_id = pr.prototype_id inner join region r on pr.region_id = r.region_id where region_name like '%s'"%(search)
    result = [i for i in opsql.select(sql, conn_info)]
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"] = row[1]
        dic_one_person_info["servent_profile_pic"] = row[2]
        dic_info.append(dic_one_person_info)
    return dic_info


def origin_search(origin,conn_info=c.get_now_conn()):
    search = '%'
    for i in origin:
        search += i
        search += '%'
    sql = "select s.servent_id,servent_name,profile_pic from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype p on sp.prototype_id=p.prototype_id inner join servent_profile_pic spp on s.servent_id = spp.servent_id inner join prototype_origin po on p.prototype_id = po.prototype_id inner join origin o on po.origin_id = o.origin_id where origin_name like '%s'"%(search)
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
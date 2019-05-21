from basic_sql_op import op_database as opsql

'''
按源类型查询相关英灵
input: 原型
output: 按照json格式返回与该原型有关的所有英灵id,姓名，图片网址。
'''
def prototype_search(prototype):
    db = opsql.Database()
    search = '%'
    for i in prototype:
        search += i
        search += '%'
    sql = "select s.servent_id,servent_name,profile_pic from servent s " \
          "inner join servent_and_prototype sp on s.servent_id=sp.servent_id " \
          "inner join prototype p on sp.prototype_id=p.prototype_id " \
          "inner join servent_profile_pic spp on s.servent_id = spp.servent_id " \
          "where prototype_name like %s;"
    result = db.select(sql,[search])
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"] = row[1]
        dic_one_person_info["servent_profile_pic"] = row[2]
        dic_info.append(dic_one_person_info)
    db.close()
    return dic_info

'''
按地域名查询相关英灵
input: 地域名
output: 按照json格式返回与该地域名有关的所有英灵id,姓名，图片网址。
'''
def region_search(region):
    db = opsql.Database()
    search= '%'
    for i in region:
        search += i
        search += '%'
    sql = "select s.servent_id,servent_name,profile_pic from servent s " \
          "inner join servent_and_prototype sp on s.servent_id=sp.servent_id " \
          "inner join prototype p on sp.prototype_id=p.prototype_id " \
          "inner join servent_profile_pic spp on s.servent_id = spp.servent_id " \
          "inner join prototype_and_region pr on p.prototype_id = pr.prototype_id " \
          "inner join region r on pr.region_id = r.region_id " \
          "where region_name like %s;"
    result = db.select(sql,[search])
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"] = row[1]
        dic_one_person_info["servent_profile_pic"] = row[2]
        dic_info.append(dic_one_person_info)
    db.close()
    return dic_info

'''
按起源查询相关英灵
input: 起源
output: 按照json格式返回与该起源有关的所有英灵id,姓名，图片网址。
'''
def origin_search(origin):
    db = opsql.Database()
    search = '%'
    for i in origin:
        search += i
        search += '%'
    sql = "select s.servent_id,servent_name,profile_pic from servent s " \
          "inner join servent_and_prototype sp on s.servent_id=sp.servent_id " \
          "inner join prototype p on sp.prototype_id=p.prototype_id " \
          "inner join servent_profile_pic spp on s.servent_id = spp.servent_id " \
          "inner join prototype_and_origin po on p.prototype_id = po.prototype_id " \
          "inner join origin o on po.origin_id = o.origin_id " \
          "where origin_name like %s;"
    result = db.select(sql,[search])
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"] = row[1]
        dic_one_person_info["servent_profile_pic"] = row[2]
        dic_info.append(dic_one_person_info)
    db.close()
    return dic_info


#print(name_search("兰陵王",c.conn2_info))
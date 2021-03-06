from basic_sql_op import op_database as opsql

'''
按特征查询相关英灵
input: 英灵起源，地域，类型，结盟，体重范围，身高范围
output: 按照json格式返回获得该英灵的id,servent_name,servent_profile_pic属性。
'''
def characteristic_search(info,weight,height):
    db = opsql.Database()
    para=[]
    select_sql="where "
    for key in info:
        if not info[key]=='null':
            select_sql+=key+"=%s and "
            para.append(info[key])
    select_sql+="height>=%s and height<=%s and weight>=%s and weight<=%s"
    para.extend([str(height[0]),str(height[1]),str(weight[0]),str(weight[1])])
    sql='select s.servent_id,s.servent_name from servent s ' \
        'inner join servent_and_prototype sp on s.servent_id=sp.servent_id ' \
        'inner join prototype_and_origin po on sp.prototype_id=po.prototype_id ' \
        'inner join prototype_and_region pr on sp.prototype_id=pr.prototype_id ' \
        'inner join region r on pr.region_id=r.region_id ' \
        'inner join origin o on po.origin_id=o.origin_id ' \
        'inner join servent_and_alignment sa on sa.servent_id=s.servent_id ' \
        'inner join alignment a on a.alignment_id=sa.alignment_id ' \
        'inner join servent_and_class sac on sac.servent_id=s.servent_id ' \
        'inner join class c on sac.class_id=c.class_id '
    sql+=select_sql+" group by s.servent_id;"
    result = db.select(sql,para)
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"]=row[1]
        servent_profile_pic_sql="select profile_pic from servent_profile_pic where servent_id=%s;"
        dic_one_person_info["servent_profile_pic"] = [i[0] for i in db.select(servent_profile_pic_sql,[row[0]])][0]
        dic_info.append(dic_one_person_info)
    db.close()
    return dic_info

'''
特定所有属性获取
output: 按照json格式返回数据库中已存在的所有地域，起源，结盟，类型信息。
'''
def get_attribute():
    db = opsql.Database()
    dic_info = {}  # 4个list
    region_sql="select region_name from region;"
    origin_sql ="select origin_name from origin;"
    alignment_sql ="select alignment_name from alignment;"
    servent_class_sql ="select class_name from class;"
    dic_info['region']=[i[0] for i in db.select(region_sql,[])]
    dic_info['origin'] =[i[0] for i in db.select(origin_sql,[])]
    dic_info['alignment'] =[i[0] for i in db.select(alignment_sql,[])]
    dic_info['servent_class'] =[i[0] for i in db.select(servent_class_sql,[])]
    db.close()
    return dic_info
from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
def characteristic_search(info,weight,height,conn_info=c.conn3_info):
    select_sql="where "
    for key in info:
        if not info[key]=='null':
            select_sql+="%s='%s' and "%(key,info[key])

    select_sql+="height>=%d and height<=%d and weight>=%d and weight<=%d"%(weight[0],weight[1],height[0],height[1])
    sql="select s.servent_id,s.servent_name from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype_origin po on sp.prototype_id=po.prototype_id inner join prototype_region pr on sp.prototype_id=pr.prototype_id inner join region r on pr.region_id=r.region_id inner join origin o on po.origin_id=o.origin_id inner join servent_alignment sa on sa.servent_id=s.servent_id inner join alignment a on a.alignment_id=sa.alignment_id inner join servent_and_class sac on sac.servent_id=s.servent_id inner join class c on sac.class_id=c.class_id "
    sql+=select_sql
    sql +=" group by s.servent_id"
    result = [i for i in opsql.select(sql,conn_info)]
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"]=row[1]
        dic_one_person_info["servent_profile_pic"] = [i[0] for i in opsql.select( "select profile_pic from servent_profile_pic where servent_id='%s'" % (row[0]),conn_info)][0]
        dic_info.append(dic_one_person_info)
    return dic_info

def get_attribute(conn_info=c.conn3_info):

    dic_info = {}  # 4个list
    region_sql="select region_name from region"
    origin_sql ="select origin_name from origin"
    alignment_sql ="select alignment_name from alignment"
    servent_class_sql ="select class_name from class"
    dic_info['region']=[i[0] for i in opsql.select(region_sql, conn_info)]
    dic_info['origin'] =[i[0] for i in opsql.select(origin_sql, conn_info)]
    dic_info['alignment'] =[i[0] for i in opsql.select(alignment_sql, conn_info)]
    dic_info['servent_class'] =[i[0] for i in opsql.select(servent_class_sql, conn_info)]
    return dic_info

def t1():
    info = {}
    info['origin_name'] = '史实'
    info['region_name'] = '中国'
    info['class_name'] = 'Rider'
    info['alignment_name'] = '中立·中庸'
    weight = [2,500]
    height = [2,500]
    print(characteristic_search(info,weight,height,c.conn2_info))

def t2():
    info = {}
    info['origin_name'] = 'null'
    info['region_name'] = '中国'
    info['class_name'] = 'Rider'
    info['alignment_name'] = '中立·中庸'
    weight = [2,500]
    height = [2,500]
    print(characteristic_search(info,weight,height,c.conn2_info))

def t3():
    info = {}
    info['origin_name'] = 'null'
    info['region_name'] = 'null'
    info['class_name'] = 'null'
    info['alignment_name'] = '中立·中庸'
    weight = [2,500]
    height = [2,500]
    print(characteristic_search(info,weight,height,c.conn2_info))

#t1()
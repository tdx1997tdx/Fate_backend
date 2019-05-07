from basic_sql_op import op_postgresql as opsql
import basic_sql_op.conn_sql as c
def characteristic_search(info,weight,height,conn_info=c.get_now_conn()):
    select_sql="where "
    para=[]
    for key in info:
        if not info[key]=='null':
            select_sql+="%s='%s' and "
            para.append(key)
            para.append(info[key])
    select_sql+="height>=%s and height<=%s and weight>=%s and weight<=%s"
    para.append(str(weight[0]))
    para.append(str(weight[1]))
    para.append(str(height[0]))
    para.append(str(height[1]))
    sql="select s.servent_id,s.servent_name from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype_origin po on sp.prototype_id=po.prototype_id inner join prototype_region pr on sp.prototype_id=pr.prototype_id inner join region r on pr.region_id=r.region_id inner join origin o on po.origin_id=o.origin_id inner join servent_alignment sa on sa.servent_id=s.servent_id inner join alignment a on a.alignment_id=sa.alignment_id inner join servent_and_class sac on sac.servent_id=s.servent_id inner join class c on sac.class_id=c.class_id "
    sql+=select_sql
    sql +=" group by s.servent_id"
    result = [i for i in opsql.select(sql,para,conn_info)]
    dic_info = []  # 所有人
    for row in result:
        dic_one_person_info = {}  # 单个人
        dic_one_person_info['id'] = str(row[0])
        dic_one_person_info["servent_name"]=row[1]
        dic_one_person_info["servent_profile_pic"] = [i[0] for i in opsql.select( "select profile_pic from servent_profile_pic where servent_id='%s'" % (row[0]),conn_info)][0]
        dic_info.append(dic_one_person_info)
    return dic_info

def get_attribute(conn_info=c.get_now_conn()):

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
from basic_sql_op import op_postgresql as opsql
import basic_sql_op.conn_sql as c
import random
def servent_infomation(id,conn_info=c.get_now_conn()):
    sql="select * from servent where servent_id='%s'"%(id)
    result = [i for i in opsql.select(sql,conn_info)]
    dic_info = {}
    row=result[0]
    dic_info['servent_id'] = row[0]
    dic_info['servent_name'] = row[1]
    dic_info['servent_name_japanese'] = row[2]
    dic_info['servent_name_english'] = row[3]
    dic_info['height'] = row[4]
    dic_info['weight'] = row[5]
    dic_info['gender'] = row[6]
    dic_info['strength'] = row[7]
    dic_info['endurance'] = row[8]
    dic_info['agility'] = row[9]
    dic_info['mana'] = row[10]
    dic_info['luck'] = row[11]
    dic_info['noble_phantasm'] = row[12]
    dic_info['craft_name'] = row[13]
    dic_info['craft_description'] = row[14].replace('\n','')
    dic_info['craft_src'] = row[15]
    alignment_sql="select alignment_name from servent_alignment sa inner join alignment a on sa.alignment_id=a.alignment_id where servent_id='%s'" % (id)
    alignment_res=[i[0] for i in opsql.select(alignment_sql, conn_info)]
    dic_info["alignment"] = alignment_res[random.randint(0,len(alignment_res)-1)] if alignment_res!=[] else 'unknown'
    class_sql = "select class_name from servent_and_class sc inner join class c on sc.class_id=c.class_id where servent_id='%s'" % (id)
    class_res=[i[0] for i in opsql.select(class_sql, conn_info)]
    dic_info["class"] = class_res[random.randint(0,len(class_res)-1)]if class_res!=[] else 'unknown'
    illustrator_sql = "select illustrator_name from servent_illustrator si inner join illustrator i on si.illustrator_id=i.illustrator_id where servent_id='%s'" % (id)
    illustrator_res=[i[0] for i in opsql.select(illustrator_sql, conn_info)]
    dic_info["illustrator"] = illustrator_res[random.randint(0,len(illustrator_res)-1)]if illustrator_res!=[] else 'unknown'
    voice_actor_sql = "select voice_actor_name from servent_voice_actor sva inner join voice_actor va on sva.voice_actor_id=va.voice_actor_id where servent_id='%s'" % (id)
    voice_actor_res=[i[0] for i in opsql.select(voice_actor_sql,conn_info)]
    dic_info["voice_actor"] = voice_actor_res[random.randint(0,len(voice_actor_res)-1)]if voice_actor_res!=[] else 'unknown'
    bond_text_sql = "select bond_text from servent_bond where servent_id='%s'" % (id)
    dic_info["bond_text"] = [i[0].replace('\n','') for i in opsql.select(bond_text_sql, conn_info)]
    full_picture_sql="select servent_picture from servent_full_pic where servent_id='%s'" % (id)
    full_picture_res=[i[0] for i in opsql.select(full_picture_sql, conn_info)]
    dic_info["full_picture"] = full_picture_res[random.randint(0,len(full_picture_res)-1)]if full_picture_res!=[] else 'unknown'
    big_sql = "select region_name,origin_name,prototype_name from servent_prototype sp inner join prototype p on sp.prototype_id=p.prototype_id inner join prototype_origin po on sp.prototype_id=po.prototype_id inner join prototype_region pr on sp.prototype_id=pr.prototype_id inner join region r on pr.region_id=r.region_id inner join origin o on po.origin_id=o.origin_id where servent_id='%s'" % (id)
    res=[i for i in opsql.select(big_sql, conn_info)]
    region_res=list(set([i[0] for i in res]))
    origin_res=list(set([i[1] for i in res]))
    prototype_res=list(set([i[2] for i in res]))
    dic_info["region"] = region_res[random.randint(0,len(region_res)-1)]if region_res!=[] else 'unknown'
    dic_info["origin"] = origin_res[random.randint(0,len(origin_res)-1)]if origin_res!=[] else 'unknown'
    dic_info["prototype"] = prototype_res[random.randint(0,len(prototype_res)-1)]if prototype_res!=[] else 'unknown'
    return dic_info

#print(servent_infomation('19',c.conn2_info))
from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
id='1'
sql = "select isnull(voice_actor_name,'unkown') from servent_voice_actor sva inner join voice_actor va on sva.voice_actor_id=va.voice_actor_id where servent_id='%s'" % (id)
result =[i for i in opsql.select(sql,c.conn4_info)]
print(result)



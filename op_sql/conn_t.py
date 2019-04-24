from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
sql="select servent_name,origin,region,alignment from servent s inner join servent_prototype sp on s.servent_id=sp.servent_id inner join prototype_origin po on sp.prototype_id=po.prototype_id inner join prototype_region pr on sp.prototype_id=pr.prototype_id inner join region r on pr.region_id=r.region_id inner join origin o on po.origin_id=o.origin_id inner join servent_alignment sa on sa.servent_id=s.servent_id inner join alignment a on a.alignment_id=sa.alignment_id"
result =[i for i in opsql.select(sql,c.conn2_info)]
for i in result:
    print(i)



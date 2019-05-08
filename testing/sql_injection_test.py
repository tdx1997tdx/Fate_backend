from basic_sql_op import op_database as opsql
db = opsql.Database(opsql.conn2_info)
str="1 or 1=1;"
sql = "select * from author where author_id=%s"
sql2 = "select * from author where contains(author_name,超)"
print(sql)
result = db.select(sql,[str])
print(result)



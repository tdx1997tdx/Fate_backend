import psycopg2
import basic_sql_op.conn_sql as c
conn_info=c.conn2_info
conn = psycopg2.connect(database=conn_info[0], user=conn_info[1], password=conn_info[2], host=conn_info[3], port=conn_info[4])
cursor = conn.cursor()
id="1 or 1=1;"
# 执行SQL语句
sql = "select * from author where author_id=%s"
sql2 = "select * from author where contains(author_name,超)"
print(sql)
cursor.execute(sql,[id])
#cursor.execute(sql2)
# 获取所有记录列表
results = cursor.fetchall()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
print(results)



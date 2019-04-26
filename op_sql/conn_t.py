from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
region_id='38'
sql = "select a.article_id,article_title,article_content,author_name from region_and_article raa inner join article a on raa.article_id=a.article_id inner join author_and_article aaa on a.article_id=aaa.article_id inner join author au on aaa.author_id=au.author_id where region_id='%s'" % (
        region_id)
result =[i for i in opsql.select(sql,c.conn2_info)]
for i in result:
    print(i)



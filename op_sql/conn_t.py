from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
region_id='33'
origin_id='52'
sql  = "select book_name,isbn,writer_name from book b inner join book_and_writer baw on b.book_id=baw.book_id inner join writer w on w.writer_id=baw.writer_id where b.book_id in (select region_book.book_id from region_book where region_id=33 union select origin_book.book_id from origin_book where origin_id=52)"
result =[i for i in opsql.select(sql,c.conn2_info)]
for i in result:
    print(i)



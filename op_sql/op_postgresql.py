import psycopg2
import op_sql.conn_sql as c
def select(sql,conn_info=c.get_now_conn()):
    conn = psycopg2.connect(database=conn_info[0], user=conn_info[1], password=conn_info[2], host=conn_info[3], port=conn_info[4])
    cursor = conn.cursor()
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        yield row
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def insert(sql,conn_info=c.get_now_conn()):
    conn = psycopg2.connect(database=conn_info[0], user=conn_info[1], password=conn_info[2], host=conn_info[3],
                            port=conn_info[4])
    cursor = conn.cursor()
    # 执行SQL语句
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        # 发生错误时回滚
        conn.rollback()
        return False
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return True

def update(sql,conn_info=c.get_now_conn()):
    conn = psycopg2.connect(database=conn_info[0], user=conn_info[1], password=conn_info[2], host=conn_info[3],
                            port=conn_info[4])
    cursor = conn.cursor()
    # 执行SQL语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        return False
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return True

def delete(sql,conn_info=c.get_now_conn()):
    conn = psycopg2.connect(database=conn_info[0], user=conn_info[1], password=conn_info[2], host=conn_info[3],
                            port=conn_info[4])
    cursor = conn.cursor()
    # 执行SQL语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        return False
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return True

import psycopg2
conn1_info = ("ubuntu", "ubuntu", "123456", "127.0.0.1", "5432")
conn2_info = ("ubuntu", "ubuntu", "123456", "122.152.251.171", "5432")
class Database:

    def __init__(self,conn_info=conn1_info):
        self.conn_info=conn_info
        self.connection = psycopg2.connect(database=self.conn_info[0], user=self.conn_info[1],
                                           password=self.conn_info[2], host=self.conn_info[3],
                                           port=self.conn_info[4])
        self.cursor =self.connection.cursor()

    '''
    用于连接数据库，创建游标
    '''
    def connect(self):
        self.connection = psycopg2.connect(database=self.conn_info[0], user=self.conn_info[1],
                                           password=self.conn_info[2], host=self.conn_info[3],
                                           port=self.conn_info[4])
        self.cursor = self.connection.cursor()

    '''
    用于关闭数据库连接
    '''
    def close(self):
        self.cursor.close()
        self.connection.close()

    '''
    用于查询数据库中的相关信息
    input: sql语句，参数
    output: 查询结果
    '''
    def select(self,sql,para):
        # 执行SQL语句
        try:
            self.cursor.execute(sql,para)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            if results==():
                return []
            return results
        except Exception as e:
            print(e)
            return []


    '''
    用于增加，删除，修改数据库中的相关信息
    input: sql语句，参数
    output: 修改结果成功True或失败False
    '''
    def iur(self,sql,para):
        try:
            self.cursor.execute(sql,para)
            self.connection.commit()
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.connection.rollback()
            return False
        return True

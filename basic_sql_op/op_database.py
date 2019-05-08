import psycopg2

class Database:
    conn1_info = ("ubuntu", "ubuntu", "123456", "127.0.0.1", "5432")
    conn2_info = ("ubuntu", "ubuntu", "123456", "122.152.251.171", "5432")
    def __init__(self):
        self.connection = psycopg2.connect(database=self.get_now_info()[0], user=self.get_now_info()[1],
                                           password=self.get_now_info()[2], host=self.get_now_info()[3],
                                           port=self.get_now_info()[4])
        self.cursor =self.connection.cursor()

    def connect(self):
        self.connection = psycopg2.connect(database=self.get_now_info()[0], user=self.get_now_info()[1],
                                           password=self.get_now_info()[2], host=self.get_now_info()[3],
                                           port=self.get_now_info()[4])
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def get_now_info(self):
        return self.conn1_info

    def select(self,sql,para):
        # 执行SQL语句
        try:
            self.cursor.execute(sql,para)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return []

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

import pymysql.cursors
class MySQLPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='172.17.149.22',  # 数据库地址
            port=3306,  # 数据库端口
            db='felink_poetry_db_test',  # 数据库名
            user='mobileuser',  # 数据库用户名
            passwd='mobileuserpws',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            "insert into position (position_name,position_link,position_type,people_num,work_location,publish_time) value (%s,%s,%s,%s,%s,%s)",
            (item['positionname'],item["positionlink"],item["positionType"],item["peopleNum"],item["workLocation"],item["publishTime"])
        )
        self.connect.commit()
        return item
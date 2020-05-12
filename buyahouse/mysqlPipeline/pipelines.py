import json
from buyahouse import settings
import pymysql
from buyahouse.mysqlPipeline.sql import lianjiaSql
from buyahouse.items import BuyahouseItem


MYSQL_HOSTS = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host = MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor()

class SzLianjiaErPipeline(object):
    def __init__(self):
        self.file = open('ershoufang.json', 'w', encoding='utf-8')

    @classmethod
    def insert_er_house(cls, item):
        sql = 'INSERT INTO sz_house (`houselink`) VALUES (%(url)s)'
        value = {
            'url': item['url']
        }
        cur.execute(sql, value)
        cnx.commit()

    def process_item(self, item, spider):

        if isinstance(item, BuyahouseItem):
            SzLianjiaErPipeline.insert_er_house(item)
            # self.file = open('ershoufang.json', 'w')
            print('=======处理深圳二手房=========')
            content = json.dumps(dict(item), ensure_ascii=False)+"\n"
            self.file.write(content)
            # print("已经写入.json文件")
            # return item
        # elif isinstance(item, SzLianjiaItem):
        #     print('处理深圳新房')

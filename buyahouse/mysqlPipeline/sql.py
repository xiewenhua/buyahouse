import pymysql
from buyahouse import settings

MYSQL_HOSTS = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host = MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor()

class lianjiaSql:
    @classmethod
    def insert_er_house(cls, **dict_data):
        sql = 'INSERT INTO sz_house (`url`) VALUES (%(url)s)'
        value = {
            'url': dict_data['url']
        }
        cur.execute(sql, value)
        cur.commit()

    @classmethod
    def update_er_house(cls):
        return None
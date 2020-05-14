import json
from buyahouse import settings
import pymysql
from buyahouse.mysqlPipeline.sql import lianjiaSql
from buyahouse.items import BuyahouseItem
import re

MYSQL_HOSTS = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,
                      host=MYSQL_HOSTS, database=MYSQL_DB, charset="utf8")
cur = cnx.cursor()
# cur.execute("SET NAMES utf8")

# 中文写不进去调试
# cur.execute("SET NAMES utf8")


class SzLianjiaErPipeline(object):
    def __init__(self):
        self.file = open('ershoufang.json', 'w', encoding='utf-8')

    @classmethod
    def separate_values(cls, str):
        try:
            return re.findall(r"\d+\.\d+|\d+", str)[0]
        except:
            # print("提取数值错误（"+str+")")
            return None

    @classmethod
    def equipped_with_elevator(cls, str):
        return str == "有"

    @classmethod
    def str_or_none(cls, str):
        if str:
            return str[0]
        else:
            return None

    @classmethod
    def insert_er_house(cls, item):
        sql = """ 
            INSERT INTO sz_house(
                houselink,
                title,
                price,
                price_per_square,
                community_name,
                area,
                linknumber,
                housing_type,
                construction_area,
                inside_area,
                house_orientation,
                renovation_condition,
                equipped_with_elevator,
                floor_area,
                total_floor,
                unit_structure,
                building_structure,
                staircase_ratio,
                room_spare_parts,
                owner_ship,
                usage_of_houses,
                transaction_ownership,
                housing_society_code,
                mortgage_information,
                housing_years,
                last_transaction,
                listing_time
            )
            VALUES(
                %(houselink)s,
                %(title)s,
                %(price)s,
                %(price_per_square)s,
                %(community_name)s,
                %(area)s,
                %(linknumber)s,
                %(housing_type)s,
                %(construction_area)s,
                %(inside_area)s,
                %(house_orientation)s,
                %(renovation_condition)s,
                %(equipped_with_elevator)s,
                %(floor_area)s,
                %(total_floor)s,
                %(unit_structure)s,
                %(building_structure)s,
                %(staircase_ratio)s,
                %(room_spare_parts)s,
                %(owner_ship)s,
                %(usage_of_houses)s,
                %(transaction_ownership)s,
                %(housing_society_code)s,
                %(mortgage_information)s,
                %(housing_years)s,
                %(last_transaction)s,
                %(listing_time)s
            )
            """
        value = {
            "houselink": item['houselink'],
            "title": item['title'][0],
            "price": SzLianjiaErPipeline.separate_values(item['price'][0]),
            "price_per_square": SzLianjiaErPipeline.separate_values(item['price_per_square'][0]),
            "community_name": item['community_name'][0],
            "area": item['area'][0],
            "linknumber": int(item['linknumber'][0]),
            "housing_type": item['housing_type'][0],
            "construction_area": SzLianjiaErPipeline.separate_values(item['construction_area'][0]),
            "inside_area": SzLianjiaErPipeline.separate_values(item['inside_area'][0]),
            "house_orientation": item['house_orientation'][0],
            "renovation_condition": item['renovation_condition'][0],
            "equipped_with_elevator": SzLianjiaErPipeline.equipped_with_elevator(item['equipped_with_elevator'][0]),
            "floor_area": item['house_floor'][0][:1],
            "total_floor": SzLianjiaErPipeline.separate_values(item['house_floor'][0]),
            "unit_structure": item['unit_structure'][0],
            "building_structure": item['building_structure'][0],
            "staircase_ratio": item['staircase_ratio'][0],
            "room_spare_parts": item['room_spare_parts'][0],
            "owner_ship": item['owner_ship'][0],
            "usage_of_houses": item['usage_of_houses'][0],
            "transaction_ownership": item['transaction_ownership'][0],
            "housing_society_code": SzLianjiaErPipeline.str_or_none(item['housing_society_code']),
            "mortgage_information": item['mortgage_information'][0].strip(),
            "housing_years": item['housing_years'][0],
            "last_transaction": item['last_transaction'][0],
            "listing_time": item['listing_time']
        }

        try:
            cur.execute(sql, value)
        except:
            print("-------写入MySQL出错-------")
            print(cur._last_executed)
        else:
            cnx.commit()
            # print("-------写入数据库成功---------")

    def process_item(self, item, spider):

        if isinstance(item, BuyahouseItem):
            SzLianjiaErPipeline.insert_er_house(item)
            # self.file = open('ershoufang.json', 'w')
            # print('=======处理深圳二手房=========')
            content = json.dumps(dict(item), ensure_ascii=False)+"\n"
            self.file.write(content)
            # print("已经写入.json文件")
            # return item
        # elif isinstance(item, SzLianjiaItem):
        #     print('处理深圳新房')

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BuyahouseItem(scrapy.Item):
    '''深圳二手房Item'''

    # 详情链接
    houselink = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 价格(int)
    price = scrapy.Field()
    # 每平价格(int)
    price_per_square = scrapy.Field()
    # 小区名称
    community_name = scrapy.Field()
    # 所在区域（列表类型比如["南山区","科技园"]）
    area = scrapy.Field()
    # 链家编号(bigint)
    linknumber = scrapy.Field()

    # 房屋户型
    housing_type = scrapy.Field()
    # 建筑面积(int,提取数字)
    construction_area = scrapy.Field()
    # 套内面积(int，提取数字)
    inside_area = scrapy.Field()
    # 房屋朝向
    house_orientation = scrapy.Field()
    # 装修情况
    renovation_condition = scrapy.Field()
    # 配备电梯(BOOL，有--->1)
    equipped_with_elevator = scrapy.Field()
    # 所在楼层("高楼层（共31层"--->>>楼层区域：高， 总楼层：31（int)
    house_floor = scrapy.Field()
    # 户型结构
    unit_structure = scrapy.Field()
    # 建筑结构
    building_structure = scrapy.Field()
    # 梯户比例
    staircase_ratio = scrapy.Field()

    # 挂牌时间(data)
    listing_time = scrapy.Field()
    # 上次交易(data)
    last_transaction = scrapy.Field()
    # 房屋年限(varchar)
    housing_years = scrapy.Field()
    # 抵押信息
    mortgage_information = scrapy.Field()
    # 房协编码
    housing_society_code = scrapy.Field()
    # 交易权属
    transaction_ownership = scrapy.Field()
    # 房屋用途
    usage_of_houses = scrapy.Field()
    # 产权所属
    owner_ship = scrapy.Field()
    # 房本备件
    room_spare_parts = scrapy.Field()

# from .sql import lianjiaSql
from buyahouse.items import BuyahouseItem
import json


class SzLianjiaErPipeline(object):
    def __init__(self):
        self.file = open('ershoufang.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        if isinstance(item, BuyahouseItem):
            # self.file = open('ershoufang.json', 'w')
            # print('=======处理深圳二手房=========')
            content = json.dumps(dict(item), ensure_ascii=False)+"\n"
            self.file.write(content)
            # print("已经写入.json文件")
            # return item
        # elif isinstance(item, SzLianjiaItem):
        #     print('处理深圳新房')

import json



class SzHouseErPipeline:
    """二手房"""
    
    def __init__(self):
        self.file=open('ershoufang.json','w')

    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(content)
        print("已经写入.json文件")
        return item


class SzHousePipeline:
    '''新房'''
    def process_item(self, item, spider):
        print(2222)
        return item
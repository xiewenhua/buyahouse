# buyahouse
实时监控房价


## TODO


1. 编写spiders， 本地开发数据以json格式保存，后期储存到mysql
2. 待定

## 如何运行

1. 确保Scrapy、PyMySQL、Python等环境已安装

2. 创建数据库，确保数据库和setting.py文件对应配置一致，进入数据库创建表

    `source <create.sql路径文件>`

3. 在本文件README.md 同级目录下打开命令行输入
   
    `scrapy crawl sz`

4. 验证数据已经爬下来，进入数据库

    `select * from debug_view`











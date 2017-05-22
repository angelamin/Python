## 安装Scrapy
>pip install scrapy

## 使用
创建一个新的Scrapy项目
>scrapy startproject tutorial

scrapy.cfg: 项目的配置文件
tutorial/: 该项目的python模块。之后您将在此加入代码。
tutorial/items.py: 项目中的item文件.
tutorial/pipelines.py: 项目中的pipelines文件.
tutorial/settings.py: 项目的设置文件.
tutorial/spiders/: 放置spider代码的目录.

>scrapy crawl dmoz -o items.json

该命令将采用 JSON 格式对爬取的数据进行序列化，生成 items.json 文件。

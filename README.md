# Stock-catchbat
中国债券信息网爬虫程序

## 功能
网页：https://www.chinabond.com.cn/

每隔一小时进行网页抓取，循环抓取，收到中断的指令则退出循环。判断网页更新内容，对更新的超链接标题的标题文本内容进行弹框。

## 依赖库
爬虫：urllib.request, bs4.BeautifulSoup

数据处理：pandas库

可视化输出： tkinter




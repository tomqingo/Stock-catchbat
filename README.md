# Stock-catchbat
中国债券信息网爬虫程序

## 功能
网页：https://www.chinabond.com.cn/

每隔一小时进行网页抓取，循环抓取，收到中断的指令则退出循环。判断网页更新内容，对更新的超链接标题的标题文本内容进行弹框。

由于对于不同信息爬取主要是其中tag的atrribute不一样，所以爬虫程序只爬取了该网页中重点关注、最新发布、企业债受理信息与发行与付息兑付四部分信息，作为展示。当然可以拓展到其他部分。

## 依赖库
爬虫：urllib.request, bs4.BeautifulSoup

数据处理：pandas库

可视化输出： tkinter

## 具体函数定义
CatchInfo——爬虫模块

checkNewInsert——查看哪些是新插入的，在之前保存excel中

showNewsInfo——弹框显示最新新闻

catchMain——爬虫主程序

## 结果
![Result](https://github.com/tomqingo/Stock-catchbat/blob/main/result.png)



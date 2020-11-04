from urllib import request
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import threading
import tkinter
import tkinter.messagebox as ms
#from mttkinter import  mtTkinter as tk

#爬虫的模块
def CatchInfo(bs,idDict):
	CatchdataList = []
	for ul_tag in bs.find_all('div', idDict):
		for li_tag in ul_tag.find_all('ul'):
			for span_tag in li_tag.find_all('li', {'class':''}):
				date_tag = span_tag.find('em', {'class': 'date'})
				if date_tag is not None:
					date = date_tag.text.strip()
				else:
					date = span_tag.text.strip()
				content_tag = span_tag.find('a')
				content = content_tag.get('title')
				if date == None or content == None:
					continue
				else:
					NewItem = {'Time':date,'Title':content}
					CatchdataList.append(NewItem)
	return CatchdataList

# 查看哪些是新插入的东西
def checkNewInsert(CatchDataSave,ExistingData):
	NewInsertCol = []
	for ii in range(len(CatchDataSave)):
		itemContent = CatchDataSave[ii]['Title']
		if itemContent in ExistingData:
			continue
		else:
			NewInsertCol.append(itemContent)
	return NewInsertCol

# 弹框显示最新新闻
def showNewsInfo(CatchdataSave):
	string = ''
	if len(CatchdataSave)>0:
		for titleIndex in range(len(CatchdataSave)):
			title = CatchdataSave[titleIndex]
			if titleIndex > 0:
				string = string+'\r\n'
			string = string + title
		top = tkinter.Tk()
		top.withdraw()
		top.update()
		txt = ms.askyesno('News',string)
		top.destroy()


# 循环爬虫，每隔一小时一次，并且保存到csv文件中
def catchMain():
	url = 'https://www.chinabond.com.cn/'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
	idList = [{'id': 'infolistDiv'}, {'id': 'TabTab03Con2'}, {'id': 'TabTab03Con3'}, {'id': 'TabTab03Con4'}]
	interval = 3600
	req = request.Request(url=url, headers=headers)
	html = request.urlopen(req)
	bs = BeautifulSoup(html, 'html.parser')
	CatchdataSave = []
	for idIndex in range(len(idList)):
		CatchdataList = CatchInfo(bs,idList[idIndex])
		CatchdataSave.extend(CatchdataList)
	if os.path.exists('./news.csv'):
		df = pd.read_csv('./news.csv', header=0, encoding='gbk')
		ExistingData = df['Title'].values.tolist()
		NewInsertCol = checkNewInsert(CatchdataSave, ExistingData)
		print('最新消息：')
		if len(NewInsertCol)>0:
			for ii in range(len(NewInsertCol)):
				print(NewInsertCol[ii])
			showNewsInfo(NewInsertCol)
	# 保存为DataFrame
	dataSheet = pd.DataFrame(CatchdataSave)
	print('当前消息：')
	print(dataSheet['Title'])
	dataSheet.to_csv('./news.csv')

	t = threading.Timer(interval, catchMain)
	t.start()

if __name__=="__main__":
	catchMain()
	os.remove('./news.csv')



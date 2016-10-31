How to use lhlib to build a spider for stock of "eastmoney"?

1. Create scheduler.py

	## scheduler.py
	#!-*- encoding=utf-8 -*-

	import sys
	reload(sys)
	sys.setdefaultencoding("utf-8")
	sys.path.append('/opt/lhlib')

	from emspider.emscheduler import emscheduler
	from processor import processor
	from fetcher import fetcher
	from storer import storer
	from lhspider.common import *

	class scheduler(emscheduler):
		def __init__(self, start_items):
			super(scheduler,self).__init__(start_items)
			self.fetcher = fetcher()
			self.processor = processor()
			self.storer = storer()

2. Create fetcher.py

For the data of eastmoney has been downloaded from net to lacalsystem and dealed from raw data to csv type, Here use "csv" lib to be the fetcher to read the file.

	class fetcher(emfetcher):
	def crawl(self, item, callback):
		with open(item['url'], 'rb') as csvfile:
			lines = csv.reader(csvfile)
			callback(lines, item)

3. Create processor.py

Processor is one of the most important part. It is used to format the input data to the format data.

The class "processor" should have a function named "process" and the function should return a dict type result.

	## processor.py
	#!-*- encoding=utf-8 -*-
	import sys
	sys.path.append('/opt/lhlib')

	from emspider.emprocessor import emprocessor
	import csv
	from common.switch import *
	import common.util

	class processor(emprocessor):
		def process(self, html):
			res = {}
			cnt = 0
			print html
			for line in html:
				print line
				for case in switch(cnt):
					if case(0):
						res['date'] = line
						break
					if case(1):
						res[common.util.get_pinyin('基本每股收益')] = line
						break
					if case(2):
						res[common.util.get_pinyin('扣非每股收益')] = line
						break
					if case(3):
						res[common.util.get_pinyin('稀释每股收益')] = line
						break
					if case(4):
						res[common.util.get_pinyin('净利润')] = line
						break
					if case(5):
						res[common.util.get_pinyin('净利润同比增长')] = line
						break
					if case(6):
						res[common.util.get_pinyin('净利润滚动环比增长')] = line
						break
					if case(7):
						res[common.util.get_pinyin('加权净资产收益率')] = line
						break
					if case(8):
						res[common.util.get_pinyin('摊薄净资产收益率')] = line
						break
					if case(9):
						res[common.util.get_pinyin('毛利率')] = line
						break
					if case(10):
						res[common.util.get_pinyin('实际税率')] = line
						break
					if case(11):
						res[common.util.get_pinyin('预收款')] = line
						break
					if case(12):
						res[common.util.get_pinyin('销售现金流')] = line
						break
					if case(13):
						res[common.util.get_pinyin('总资产周转率')] = line
						break
					if case(14):
						res[common.util.get_pinyin('资产负债率')] = line
						break
					if case(15):
						res[common.util.get_pinyin('流动负债')] = line
						break
					if case():
						print 'error, too much data!'
						exit()
				cnt += 1
			if cnt == 0:
				return False
			# callback(res)
			return res
				
4. Create storer.py

Storer is also one of the most important part. It is used to store the data that dealed by processor.

The input of the storer.store() should be a dict type like:

	res = {
		'content1':content1,
		'content2':content2,
		'content3':content3
	}

The function named create_table() of the class storer should create the table automaticly and the main function named store() of the class storer should detect the table automaticly and build the "sql" of Mysql automaticly.

Note: 
Because the "sql" is builded automaticly, so for solving the problem easily the project set the col type to be varchar(1024) even the integer type.

	## storer.py
	#!-*- encoding=utf-8 -*-
	import sys
	reload(sys)
	sys.setdefaultencoding("utf-8")
	sys.path.append('/opt/lhlib')

	from emspider.emstorer import *
	from common.util import *

	class storer(emstorer):
		def __init__(self):
			super(storer, self).__init__()

		def store(self, data, options):
			self.table_name = options['table']

			if not self.sql._check_table(self.table_name):
				self.create_table(data, self.table_name)

			code = options['market'] + options['code']
			t = get_cur_time()
			t_m = get_cur_time_m()
			print data

			sql_s = '''
				insert into %s(code
			'''%self.table_name
			params = []
			for k,v in data.items():
				sql_s += ", %s"%k
				params.append((k, v))
			sql_s += ', m_time, m_time_m) values("%s"'%code
			for param in params:
				v = param[1]
				sql_s += ',"' + ','.join(v) + '"'
			sql_s += ',"%s","%s"'%(t,t_m)
			sql_s +=')'
			
			print sql_s
			self.sql.insert(sql_s, self.table_name)
		
		def create_table(self, data, table_name):
			sql_s = '''
				create table %s(
					id int(32) not null AUTO_INCREMENT primary key,
					code varchar(10) not null,
			'''%table_name
			for k,v in data.items():
				sql_s += k
				sql_s += " varchar(1024),"
			sql_s += " m_time date, m_time_m int(64)"
			sql_s += ");"
			self.sql.create(sql_s, table_name)


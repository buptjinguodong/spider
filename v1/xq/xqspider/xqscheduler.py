#-*- encoding:utf-8 -*-

from lhspider.scheduler import *
from xqfetcher import *
from xqprocessor import *
import config
from lhspider.common import *
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import os



class xqscheduler(scheduler):
	def __init__(self, start_items):
		super(xqscheduler,self).__init__(start_items)
		self.fetcher = xqfetcher()
		self.processor = xqprocessor()
		self.sched = BlockingScheduler()

	def on_start_interval(self, _seconds=300):
		self.sched.add_job(self.worker, 'interval', seconds=_seconds)
		self.sched.start()

	def on_start(self):
		self.worker()

	def worker(self):
		for item in self.follows:
			print item
			self.fetcher.crawl(item, self.index_page)

	def index_page(self, response):
		# print response
		self.processor.process(response)

if __name__ == '__main__':
	hangye_url = config.xueqiu['hangye']
	# 'http://xueqiu.com/stock/industry/stockList.json?type=1&code=%s%s&size=8&_=1433829008414'%('sh','600221')
	pwd_path = os.path.dirname(__file__)
	stock_file_path = pwd_path+"/stocks"
	stocks = get_stocks(stock_file_path)
	# print stocks
	stock = stocks[0]
	code = stock[1]+stock[0]
	hangye_url = hangye_url['url']
	url = hangye_url%code
	print url
	# exit()
	init_items = [url]
	work = xqscheduler(init_items)
	work.on_start()
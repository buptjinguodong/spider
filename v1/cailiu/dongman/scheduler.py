#!-*- encoding=utf-8 -*-

import sys
sys.path.append('/opt/lhlib/xqspider')

from xqscheduler import xqscheduler
from processor import processor
from storer import *
import config
from common.util import *
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import os

class scheduler(xqscheduler):
	def __init__(self, start_items):
		super(scheduler,self).__init__(start_items)
		self.processor = processor()
		self.storer = storer()




if __name__ == '__main__':
	# Get api_url from config by name 'xxx'
	table_name = 'hangye'
	api_url = config.xueqiu[table_name]
	
	stocks = get_stocks()
	stock = stocks[0]
	
	# Build api_url to url
	code = stock[1]+stock[0]
	print api_url
	api_url = api_url['url']
	url = api_url%code
	print url

	# Build item by url, code, market, table
	item = {}
	item['url'] = url
	item['code'] = stock[0]
	item['market'] = stock[1]
	item['table'] = 'xq_%s'%table_name
	init_items = [item]
	work = scheduler(init_items)
	work.on_start()
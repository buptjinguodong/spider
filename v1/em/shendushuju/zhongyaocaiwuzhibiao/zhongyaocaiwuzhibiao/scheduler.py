#!-*- encoding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('/opt/lhlib')

from emspider.emscheduler import emscheduler
from processor import processor
from fetcher import fetcher
from storer import storer
from common.util import *

class scheduler(emscheduler):
	def __init__(self, start_items):
		super(scheduler,self).__init__(start_items)
		self.fetcher = fetcher()
		self.processor = processor()
		self.storer = storer()

if __name__ == '__main__':
	path = {}
	path['base'] = '/opt/stock/'
	path['type'] = 'eastmoney/dealed/'
	path['module'] = 'shendushuju/zhongyaocaiwuzhibiao/'
	path['file'] = 'zhongyaozhibiao'
	stocks = get_stocks()
	print stocks
	stock = stocks[0]
	url = path['base'] + stock[0] + '/' + path['type'] + path['module'] + path['file']
	item = {}
	print url
	item['url'] = url
	item['code'] = stock[0]
	item['market'] = stock[1]
	item['table'] = 'zhongyaozhibiao'
	init_items = [item]
	work = scheduler(init_items)
	work.on_start()
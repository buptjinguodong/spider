#!-*- encoding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('/opt/lhlib')

import os
from lhspider.common import *
from lirunqushi.scheduler import scheduler as lirunqushi_scheduler
from common.switch import *

class main(object):
	def __init__(self):
		self.path = {}
		self.path['base'] = '/opt/stock/'
		self.path['type'] = 'eastmoney/dealed/'
		self.path['module'] = 'shendushuju/zhongyaocaiwuzhibiao/'
		self.path['path'] = self.path['base'] + '%s/' +self.path['type'] + self.path['module']
		self.files = ['lirunqushi']
		self.files_bk = ['zhuyingyewu_hangye', 'shouruqushi', 'zhuyingyewu_hangye_detail', 'zhongyaozhibiao_detail', 'hexinticai', 'yingliqushi', 'zhuyingyewu_diqu_detail', 'qushi_detail', 'zhongyaozhibiao', 'hexinticai_detail', 'zhuyingyewu_chanpin_detail', 'dubangfenxi_detail', 'zhuyingyewu_diqu', 'lirunqushi', 'zhuyingyewu_chanpin']
		self.init_items = {}
	def start(self):
		self.pre_start()
		print self.init_items
		for f in self.files:
			for case in switch(f):
				if case('lirunqushi'):
					sch = lirunqushi_scheduler(self.init_items[f])
					sch.on_start()
					break
				if case():
					print 'nono'

	def pre_start(self):
		stocks = get_stocks()
		for f in self.files:
			f_path = self.path['path'] + f
			self.init_items[f] = []
			for stock in stocks:
				# stock = ('300292','sz')
				# stock = ('000602','sz')
				url = f_path%stock[0]
				item = {}
				item['url'] = url
				item['code'] = stock[0]
				item['market'] = stock[1]
				item['table'] = f
				self.init_items[f].append(item)
				# break
			

if __name__ == '__main__':
	m = main()
	m.start()
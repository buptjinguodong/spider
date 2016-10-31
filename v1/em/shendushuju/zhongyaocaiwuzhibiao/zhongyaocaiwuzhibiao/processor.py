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
			
		


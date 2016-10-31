#!-*- encoding=utf-8 -*-

import sys
sys.path.append('/opt/lhlib')

from emspider.emprocessor import emprocessor
import csv
from common.switch import *

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
					res['quant1'] = line
					break
				if case(2):
					res['quant2'] = line
					break
				if case(3):
					res['quant3'] = line
					break
				if case(4):
					res['quant4'] = line
					break
				if case():
					exit('error, too much data!')
			cnt += 1
		if cnt == 0:
			return False
		# callback(res)
		return res
			
		


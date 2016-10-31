#!-*- encoding=utf-8 -*-

import sys
sys.path.append('/opt/lhlib/xqspider')

from xqprocessor import xqprocessor
import json

class processor(xqprocessor):
	def process(self, html):
		print html
		response = json.loads(html)
		for (k, v) in response.items():
			if k=='industrystocks':
				for stock in v:
					print stock
					for (kk,vv) in stock.items():
						print kk, vv
			else:
				print k, v
		print 'local process'




#!-*- encoding=utf-8 -*-

import sys
sys.path.append('/opt/lhlib/xqspider')

from xqprocessor import xqprocessor
import json

class processor(xqprocessor):
	def process(self, html):
		res = {}
		response = json.loads(html)
		for (k, v) in response.items():
			if k=='totalcount':
				print k,v
				res[k] = v
		print 'local process'
		return res




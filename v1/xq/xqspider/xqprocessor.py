#-*- encoding:utf-8 -*-

from lhspider.processor import processor
from lhspider.common import *
import json
import random
import time
class xqprocessor(processor):
	def __init__(self):
		pass

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



if __name__ == '__main__':
	response = '''{"stockname":"","platename":"钢铁","industrystocks":[{"symbol":"SH601003","code":"601003","name":"柳钢股份","exchange":"SH","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"","marketCapital":"1.845211104E10"},{"symbol":"SZ000708","code":"000708","name":"大冶特钢","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"22.45","marketCapital":"6.2557660416E9"},{"symbol":"SZ000709","code":"000709","name":"河北钢铁","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"102.61","marketCapital":"7.4330254964E10"},{"symbol":"SZ000761","code":"000761","name":"本钢板材","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"128.9","marketCapital":"2.4304E10"},{"symbol":"SZ000778","code":"000778","name":"新兴铸管","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"75.29","marketCapital":"4.721726339856E10"},{"symbol":"SZ000932","code":"000932","name":"华菱钢铁","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"417.95","marketCapital":"1.420371161775E10"},{"symbol":"SZ000959","code":"000959","name":"首钢股份","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"","marketCapital":"3.252974604E10"},{"symbol":"SZ002075","code":"002075","name":"沙钢股份","exchange":"SZ","current":"0.0","percentage":"0.0","change":"0.0","volume":"0","pe_ttm":"1582.91","marketCapital":"5.2016763216E10"}],"exchange":"CN","code":"SH601005","industryname":"钢铁"}'''

	xqp = xqprocessor()
	xqp.process(response)
	
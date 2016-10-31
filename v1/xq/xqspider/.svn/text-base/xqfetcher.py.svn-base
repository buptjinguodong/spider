#-*- encoding:utf-8 -*-

from lhspider.fetcher import fetcher
from lhspider.spider import spider
from lhspider.common import *


class xqfetcher(fetcher):
	def __init__(self):
		self.sp = spider()

	def crawl(self, url, callback):
		html = self.sp.getsource_xueqiu(url)
		print html
		callback(html)



if __name__ == '__main__':
	xqf = xqfetcher()
	url = 'http://xueqiu.com/stock/industry/stockList.json?type=1&code=%s%s&size=8&_=1433829008414'%('sh','600221')
	print url
	xqf.crawl(url, p)
	
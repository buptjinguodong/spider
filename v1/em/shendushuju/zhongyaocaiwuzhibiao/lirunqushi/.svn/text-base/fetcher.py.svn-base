#!-*- encoding=utf-8 -*-

import sys
sys.path.append('/opt/lhlib/emspider')

from emfetcher import emfetcher
import csv

class fetcher(emfetcher):
	def crawl(self, item, callback):
		with open(item['url'], 'rb') as csvfile:
			lines = csv.reader(csvfile)
			callback(lines, item)

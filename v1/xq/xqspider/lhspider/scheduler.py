#-*- encoding:utf-8 -*-

from xqfetcher import xqfetcher
from xqprocessor import xqprocessor

class scheduler(object):
	def __init__(self, start_items):
		self.follows = []
		if type(start_items) != None:
			self.follows = start_items
		self.dealed = []

	def on_start(self):
		pass
	
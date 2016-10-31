#-*- encoding:utf-8 -*-

"""
this script used to read file and save file
APIs afford:
lhfile.save(file_name, string)
lhfile.read(file_name)
"""

import sys
import time
import os

reload(sys)
sys.setdefaultencoding("utf-8")

def log(class_name, function_name):
	print "error in class: " + class_name + " function: " + function_name


class lhfile(object):
	def __init__(self):
		pass
	def save(self, file_name, content):
		if os.path.exists(file_name) == False:
			file_path = os.path.dirname(file_name)
			try:
				if os.path.isdir(file_path):
					pass
				else:
					os.makedirs(file_path)
				f = open(file_name, 'w')
			except os.error, e:
				func_name = sys._getframe().f_code.co_name
				log(self.__class__, func_name)
			finally:
				f.close()

		if os.path.getsize(file_name)==0:
			try:
				f = open(file_name, 'w')
				f.write(content)
			except os.error, e:
				func_name = sys._getframe().f_code.co_name
				log(self.__class__, func_name)
			finally:
				f.close()
	def save_force(self, file_name, content):
		if os.path.exists(file_name) == False:
			file_path = os.path.dirname(file_name)
			try:
				if os.path.isdir(file_path):
					pass
				else:
					os.makedirs(file_path)
				f = open(file_name, 'w')
			except os.error, e:
				func_name = sys._getframe().f_code.co_name
				log(self.__class__, func_name)
			finally:
				f.close()
		# write the file forcely
		if os.path.getsize(file_name)>=0:
			try:
				f = open(file_name, 'w')
				f.write(content)
			except os.error, e:
				func_name = sys._getframe().f_code.co_name
				log(self.__class__, func_name)
			finally:
				f.close()

	def read(self, file_name):
		try:
			f = open(file_name, 'r')
			return f.read()
		except IOError:
			func_name = sys._getframe().f_code.co_name
			log(self.__class__, func_name)
		finally:
			f.close()
	def append(self, file_name, content):
		if os.path.exists(file_name) == False:
			file_path = os.path.dirname(file_name)
			try:
				if os.path.isdir(file_path):
					pass
				else:
					os.makedirs(file_path)
				f = open(file_name, 'w')
			except os.error, e:
				func_name = sys._getframe().f_code.co_name
				log(self.__class__, func_name)
			finally:
				f.close()

		if os.path.getsize(file_name)>=0:
			try:
				f = open(file_name, 'a')
				f.write(content)
			except os.error, e:
				func_name = sys._getframe().f_code.co_name
				log(self.__class__, func_name)
			finally:
				f.close()

	def test(self):
		print lhfile.__name__
		print dir(self)
		print self.__class__
		print self.__module__
		print self.__dict__
		print __name__
		print self.test.__name__
		func_n = sys._getframe().f_code.co_name
		print func_n


if __name__ == '__main__':
	pass
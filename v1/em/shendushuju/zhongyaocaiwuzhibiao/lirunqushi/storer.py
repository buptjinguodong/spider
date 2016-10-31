#!-*- encoding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('/opt/lhlib')

from emspider.emstorer import *
from common.util import *

class storer(emstorer):
	def __init__(self):
		super(storer, self).__init__()

	def store(self, data, options):
		self.table_name = options['table']

		if not self.sql._check_table(self.table_name):
			self.create_table(data, self.table_name)

		code = options['market'] + options['code']
		t = get_cur_time()
		t_m = get_cur_time_m()
		print data

		sql_s = '''
			insert into %s(code
		'''%self.table_name
		params = []
		for k,v in data.items():
			sql_s += ", %s"%k
			params.append((k, v))
		sql_s += ', m_time, m_time_m) values("%s"'%code
		for param in params:
			v = param[1]
			sql_s += ',"' + ','.join(v[1:]) + '"'
		sql_s += ',"%s","%s"'%(t,t_m)
		sql_s +=')'
		
		print sql_s
		self.sql.insert(sql_s, self.table_name)
	
	def create_table(self, data, table_name):
		sql_s = '''
			create table %s(
				id int(32) not null AUTO_INCREMENT primary key,
				code varchar(10) not null,
		'''%table_name
		for k,v in data.items():
			sql_s += k
			sql_s += " varchar(1024),"
		sql_s += " m_time date, m_time_m int(64)"
		sql_s += ");"
		self.sql.create(sql_s, table_name)


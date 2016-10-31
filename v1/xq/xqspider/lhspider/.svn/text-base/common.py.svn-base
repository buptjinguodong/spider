from lhfile import lhfile


def p(data):
	print data


def every(seconds=0):
	def every_decorator(f):
		def wrapper(*args, **kw):
			return f(*args, **kw)
		return wrapper
	return every_decorator()

def get_stocks(file_path):
	if type(file_path) == 'undefined':
		print 'file path undefined'
		return None
	else:
		lhf = lhfile()
		stocks = lhf.read(file_path)
		stocks = stocks.split('\n')
		_stocks = []
		for stock in stocks:
		    code = stock[0:6]
		    mk = stock[-2:]
		    # print code
		    # print mk
		    _stocks.append((code, mk))
		stocks = _stocks
		return stocks


#-*-encoding:utf8-*-
import requests
import re
import sys
import time
import json
import os
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
    	print 'begin:'
        print u'开始爬取内容。。。'
        self.s = ''
        self.xq_a_token = ''
        self.xq_r_token = ''
        self.random_seconds = 160
    def sleep_random(self, seconds):
        s_t = int(random.random()*seconds)
        print 'IP observed by xueqiu: sleep ', s_t, 's.'
        print "Token checked sleep Start time: "
        print time.asctime(time.localtime(time.time()))
        time.sleep(s_t)
        print "Token checked sleep End time: "
        print time.asctime(time.localtime(time.time()))

    def check_xueqiu_token(self, html):
        res = re.findall('(请输入验证码 - 雪球)', html, re.S)
        if len(res) > 0:
            return False
        else:
            return True

#getsource用来获取网页源代码
    def getsource(self,url, charset='gb2312'):
        html = requests.get(url)
        html.encoding = charset
        res_t = html.text.encode('utf-8')
        return res_t
    def getsource_xueqiu(self, url, charset='utf-8'):
    	headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'en-US,en;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Cookie':'s='+self.s+'; xq_a_token='+self.xq_a_token+'; xq_r_token='+self.xq_r_token+'; __utma=1.1380568153.1433482898.1433993735.1434436087.3; __utmc=1; __utmz=1.1433482898.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1433471920,1433993736,1434436088; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1434436538; route=',
			# 'Cookie':'s=hh11219gmh; xq_a_token=8212925e58009abe249b70a95bab3e464e4c6e53; xq_r_token=c40d7aa7540a8eaaa6a2aab1be5c1c0781b8cf33; __utma=1.1380568153.1433482898.1433993735.1434436087.3; __utmc=1; __utmz=1.1433482898.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1433471920,1433993736,1434436088; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1434436538; route=',
			# 'Cookie':'s=hh11219gmh; xq_a_token=843ad86506bce50f24c59d02ddb97c04dacb0db9; xq_r_token=bb280b46ec4fd16845713677e35e9d77140ae556;',
			'Host':'xueqiu.com',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    	}
    	html = requests.get(url, headers=headers)
        html.encoding = charset
        res_t = html.text.encode('utf-8')
        status = re.findall('(遇到错误，请刷新页面或者重新登录帐号后再试)', res_t, re.S)
        if len(status)>0:
        	print 'error: sleep 1s.'
        	time.sleep(1)
        	self.xueqiu_reset()
        	res_t = self.getsource_xueqiu(url, 'utf-8')
        if !self.check_xueqiu_token(res_t):
            self.sleep_random(self.random_seconds)
            self.xueqiu_reset()
            res_t = self.getsource_xueqiu(url, 'utf-8')
        # print headers
        return res_t
    def xueqiu_reset(self):
    	url = 'http://xueqiu.com'
    	headers = {
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'en-US,en;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Host':'xueqiu.com',
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    	}
    	html = requests.get(url, headers=headers)
        # print html.headers
        cks = self.xueqiu_cookie(html.headers)
        self.s = cks[0]
        self.xq_a_token = cks[1]
        self.xq_r_token = cks[2]


    def xueqiu_cookie(self, cookie=''):
    	# print cookie
    	# cookie = {'x-whom': 'hzali-ngx-228-73', 'x-powered-by': 'Express', 'transfer-encoding': 'chunked', 'set-cookie': 's=l3y1212wb7; domain=.xueqiu.com; path=/; expires=Wed, 15 Jun 2016 07:57:16 GMT; httpOnly, xq_a_token=843ad86506bce50f24c59d02ddb97c04dacb0db9; domain=.xueqiu.com; path=/; httpOnly, xq_r_token=bb280b46ec4fd16845713677e35e9d77140ae556; domain=.xueqiu.com; path=/; httpOnly, xq_is_login=; domain=xueqiu.com; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT, route=;Path=/', 'x-rt': '12', 'vary': 'Accept-Encoding', 'x-tdt': '4', 'content-encoding': 'gzip', 'x-dt': '7', 'connection': 'keep-alive', 'cache-control': 'private, no-store, no-cache, must-revalidate, max-age=0, private, no-store, no-cache, must-revalidate, max-age=0', 'date': 'Tue, 16 Jun 2015 07:57:16 GMT', 'p3p': 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"', 'content-type': 'text/html; charset=utf-8'}'''
    	# cookie.replace("'", '"')
    	# print cookie
    	ck = cookie['set-cookie']
    	# print ck
    	s = re.findall('s=(.*?);', ck, re.S)
    	s = s[0]
    	xq_a_token = re.findall('xq_a_token=(.*?);', ck, re.S)
    	xq_a_token = xq_a_token[0]
    	xq_r_token = re.findall('xq_r_token=(.*?);', ck, re.S)
    	xq_r_token = xq_r_token[0]
    	return (s, xq_a_token, xq_r_token)

if __name__ == '__main__':
    code = '601005'
    market = 'SH'
    path = './data/stock/%s/xueqiu/raw/'%(code)
    url = 'http://xueqiu.com/stock/industry/stockList.json?type=1&code=%s%s&size=8&_=1433829008414'%(market,code)
    url = 'http://xueqiu.com/statuses/topic.json?simple_user=1&filter_text=1&topicType=0&page=1'
    sp = spider()
    print url
    # sp.xueqiu_reset()
    stock_html = sp.getsource_xueqiu(url, 'utf-8')
    print stock_html
    # print sp.xueqiu_cookie()
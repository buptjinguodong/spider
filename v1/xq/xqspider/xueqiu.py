#-*- encoding:utf-8 -*-

"""本脚本用来获取xueqiu网站中 API 的内容
方法如下：
1. 首先通过 stocks 得到所有的股票编号存入 stocks
2. path = './data/stock/%s/xueqiu/raw/'%(code)
3. 从 url = 'http://f9.eastmoney.com/%s%s.html'%(market,code)
"""

import requests
import re
import sys
import time
import os
import random

reload(sys)
sys.setdefaultencoding("utf-8")

from spider import spider
from lhfile import lhfile, log
import config
from switch import switch

class xueqiu(object):
    def __init__(self):
        print "begin: "+xueqiu.__name__
        self.file_handle = lhfile()
        self.sp = spider()
        self.users_stored = []
        self.users_willbe = []

    def __str__(self):
        return 'xueqiu'

    def init(self):
        '''
        Assign users_stored by ./data/user/xueqiu/users_stored
        Assign users_willbe by ./data/user/xueqiu/users_willbe
        '''
        users_stored_file = './data/user/xueqiu/users_stored'
        users_willbe_file = './data/user/xueqiu/users_willbe'


    def _get_html(self, url, charset='utf-8'):
        html = self.sp.getsource_xueqiu(url, charset=charset)
        return html

    def _save(self, file_name, content):
        self.file_handle.save_force(file_name, content)
    def _check_token(self, html):
        res = re.findall('(请输入验证码 - 雪球)', html, re.S)
        if len(res) > 0:
            return False
        else:
            return True
    ##
    def config_xueqiu(self, configs):
        self._config = configs

    ## get data info of stock from xueqiu
    def data_of_stock(self, stock):
        '''
        get data info of a stock from xueqiu
        '''
        code = stock[0]
        market = stock[1]
        
        for key in self._config:
            print key
            val = self._config[key]
            print val
            for case in switch(val['type']):
                url = val['url']
                if case(1):
                    url = url
                elif case(2):
                    stock = market+code
                    # url.replace("\%\s\%\s", stock)
                    url = url%(stock)
                elif case(3):
                    print url%('yonghu123123')
                    # user info pass first
                    print 'user info pass first'
                    break
                elif case(4):
                    print url%('ZHZHZH')
                    print 'zuhe info pass first'
                    break
                elif case(5):
                    url = url
                # deal the data
                print 'url: ' + url
                func_name = key
                file_path = path + func_name
                print "get " + file_path
                html = self._get_html(url)
                if self._check_token(html):
                    ## everything is OK
                    self._save(file_path, html)
                else:
                    ## Have a problem that xueqiu find the IP evil
                    s_t = random.random()*60
                    print time.time()
                    time.sleep(s_t)
                    print time.time()
                    self.data_of_stock(stock)
                    print 'Token Error'
                    return 'Error'
                # print html
                
                break

    def data_of_user(self, uid):
        '''
        Get data info of a user by uid from xueqiu

        '''
        for key in self._config:
            val = self._config[key]
            for case in switch(val['type']):
                url = val['url']
                if case(3):
                    url = url%(uid)
                    print 'url: ' + url
                    func_name = key
                    file_path = path + uid + '/' + func_name
                    print "Get " + file_path
                    # html = self._get_html(url)
                    # self._save(file_path, html)
                    break

    def check_token(self):
        check_path = './data/stock/'
        check_dir = os.listdir(check_path)
        # print check_dir
        for code in check_dir:
            cd = re.findall('(\d{6})', code)
            if len(cd) == 0:
                continue
            print code
            dir_path = check_path + code + '/xueqiu/raw/'
            # print dir_path
            file_path = dir_path + 'gonggao'
            print file_path
            if os.path.isfile(file_path):
                cont = lh.read(file_path)
                res = re.findall('(请输入验证码 - 雪球)', cont, re.S)
                if len(res) > 0:
                    print 'error : %d'%len(res)
                else:
                    print 'OK'
    def check_token_by_stock(self, stocks):
        stock_dealed_file = './xueqiu_dealed_ok'

        check_path = './data/stock/'
        # check_dir = os.listdir(check_path)
        count = 0
        err_count = 0
        # print check_dir
        for stock in stocks:
            # stocks_dealed = self.file_handle.read(stock_dealed_file)
            # stocks_dealed = stocks_dealed.split('\n')
            # print stock
            # if stock[0] in stocks_dealed:
            #     continue
            code = stock[0]
            print code
            dir_path = check_path + code + '/xueqiu/raw/'
            # print dir_path
            file_path = dir_path + 'gonggao'
            print file_path
            if os.path.isfile(file_path):
                cont = lh.read(file_path)
                res = re.findall('(请输入验证码 - 雪球)', cont, re.S)
                if len(res) > 0:
                    err_count += 1
                    print 'error : %d'%err_count
                    # os.removedirs(dir_path)
                    err_files = os.listdir(dir_path)
                    print err_files
                    for err_file in err_files:
                        err_file_path = dir_path + err_file
                        print err_file_path
                        # os.remove(err_file_path)
                else:
                    count += 1
                    print 'OK : %d'%count
                    self.file_handle.append(stock_dealed_file, stock[0]+'\n')


    def test(self, stocks):
        global path
        path = './data/stock/%s/xueqiu/raw/'%(code)
        for stock in stocks:
            # self.test_login(stock)
            # self.test_by_code(stock)
            self.data_of_stock(stock)
            # break

    def test_login(self, stock):
        code = stock[0]
        market = stock[1]
        global path
        path = './data/stock/%s/xueqiu/raw/'%(code)
        url = 'http://xueqiu.com/stock/industry/stockList.json?type=1&code=%s%s&size=8&_=1433829008414'%(market,code)
        sp = spider() 
        print url
        stock_html = sp.getsource_xueqiu(url, 'utf-8')
        print stock_html
    def test_by_code(self, stock):
        # code = '600221'
        # code = '600319'
        code = stock[0]
        market = stock[1]
        print path
        dir_name = path
        
        url = 'http://xueqiu.com/stock/industry/stockList.json?type=1&code=%s%s&size=8&_=1433829008414'%(market,code)

        lh = lhfile()
        

    
    def all_user(self):
        '''
        get all of users in xueqiu
        '''
        start = p_time()

        global path
        path = './data/stock/user/xueqiu/'
        # 亿利达
        start_uid = '2164183023'
        self.data_of_user(start_uid)

        end = p_time()
        print 'start: ' + start
        print 'end: ' + end

    def all(self, stocks):
        stock_dealed_file = './xueqiu_dealed_ok'
        for stock in stocks:
            stocks_dealed = self.file_handle.read(stock_dealed_file)
            stocks_dealed = stocks_dealed.split('\n')
            print stock
            if stock[0] in stocks_dealed:
                continue
            self.all_by_code(stock)
            self.file_handle.append(stock_dealed_file, stock[0]+'\n')
            # break
    def all_by_code(self, stock):
        code = stock[0]
        market = stock[1]
        global path
        path = './data/stock/%s/xueqiu/raw/'%(code)
        self.data_of_stock(stock)

def p_time():
    p_t = time.localtime()
    return log_time(p_t)
def log_time(t):
    log_time_str = 'Time: %d/%d/%d %dh-%dm-%ds'%(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    print log_time_str
    return log_time_str

if __name__ == '__main__':
    xq = xueqiu()
    xq.config_xueqiu(config.xueqiu)
    lh = lhfile()
    code_file = './stocks'
    stocks = lh.read(code_file)
    stocks = stocks.split('\n')
    _stocks = []
    for stock in stocks:
        code = stock[0:6]
        mk = stock[-2:]
        # print code
        # print mk
        _stocks.append((code, mk))
    stocks = _stocks
    
    # xq.all(stocks)

    xq.all_user()

    # xq.check_token()
    # xq.check_token_by_stock(stocks)
    # xq.test(stocks)
    # print config.xueqiu

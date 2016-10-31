#-*- encoding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

xueqiu = {
    'yingxiangli': {'type':1, 'url':'http://xueqiu.com/cubes/discover/rank/cube/list.json?category=12&count=10&market=cn&profit=monthly_gain'},
    'renqibiaosheng': {'type':1, 'url':'http://xueqiu.com/cubes/discover/rank/cube/list.json?category=10&count=10&market=cn'},
    'zuiremenzuhe': {'type':1, 'url':'http://xueqiu.com/cubes/discover/rank/cube/list.json?category=14&page=1&count=20'},
    'gupiaodeguanzhurenshu': {'type':2, 'url':'http://xueqiu.com/recommend/pofriends.json?type=1&code=%s&start=0&count=14&_=1433829008410'},
    'hangye': {'type':2, 'url':'http://xueqiu.com/stock/industry/stockList.json?type=1&code=%s&size=8&_=1433829008414'},
    'dajiahaiguanzhu': {'type':2, 'url':'http://xueqiu.com/stock/portfolio/popstocks.json?code=%s&start=0&count=8&_=1433829008415'},
    'gupiaopinglun': {'type':2, 'url':'http://xueqiu.com/statuses/search.json?count=15&comment=0&symbol=%s&hl=0&source=all&sort=alpha&page=1&_=1433829010863'},
    'gupiaotubiaoshuju1d': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=1d&one_min=1&_=1433829011276'},
    'gupiaotubiaoshuju5d': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=5d&_=1433829011718'},
    'gupiaotubiaoshuju1m': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=1m&_=1433829011718'},
    'gupiaotubiaoshuju6m': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=6m&_=1433829011718'},
    'gupiaotubiaoshuju1y': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=1y&_=1433829011718'},
    'gupiaotubiaoshuju3y': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=3y&_=1433829011718'},
    'gupiaotubiaoshujuall': {'type':2, 'url':'http://xueqiu.com/stock/forchart/stocklist.json?symbol=%s&period=all&_=1433829011718'},
    'taolun': {'type':2, 'url':'http://xueqiu.com/statuses/search.json?count=15&comment=0&symbol=%s&hl=0&source=user&sort=time&page=1&_=1433832350713'},
    'jiaoyi': {'type':2, 'url':'http://xueqiu.com/statuses/search.json?count=15&comment=0&symbol=%s&hl=0&source=trans&page=1&_=1433832408742'},
    'zixuanguxinwen': {'type':2, 'url': 'http://xueqiu.com/statuses/stock_timeline.json?symbol_id=%s&count=200&source=自选股新闻&page=1&_=1433832434720'},
    'gonggao': {'type':2, 'url': 'http://xueqiu.com/statuses/stock_timeline.json?symbol_id=%s&count=15&source=公告&page=1&_=1433832799038'},
    'gupiaoyingxiangli': {'type':2, 'url': 'http://xueqiu.com/recommend/user/stock_hot_user.json?symbol=%s&start=0&count=60&_=1433833300928'},
    'yonghuchuangjianzuhe': {'type':3, 'url':'http://xueqiu.com/cubes/count_limit.json?user_id=%s'},
    'yonghujingchangtaolundegupiao': {'type':3, 'url':'http://xueqiu.com/user/top_status_count_stock.json?count=5&uid=%s&_=1433833728562'},
    'yonghuguanzhudegupiao': {'type':3, 'url':'http://xueqiu.com/stock/portfolio/stocks.json?size=1000&tuid=%s&_=1433833729036'},
    # yongyu chaxun gupiaoxinxi 'yonghuchaxungupiaoxinxi': {'type':3, 'http://xueqiu.com/stock/quote.json?code=ZH013472%2C01280%2C00623%2C00285%2CSZ000651%2CP000152%2CSH601336%2CSZ300058%2CSH600048%2CSZ002024%2CSZ300151%2CSZ000006%2CSH600395%2CXNET%2CSH600000%2CSH600177%2CSZ000623%2CZH000924%2CSH601607%2CSH600426%2CBABA%2CSZ000829%2CSZ150013%2CSZ000858%2CBONA%2CSH600835%2CSZ002646%2CSFUN%2CSH600410%2CSH600887%2CSH600315%2CJD%2CXRS%2CSH600196%2C00874%2CSZ300251%2CSINA%2CSH600690%2C00811%2C02039%2C01513%2CSZ002242%2CSH601166%2CSH600373%2C00700%2CSZ002697%2CSZ000002%2C03888%2CQIHU%2CSH600718%2CSZ000876%2C00656%2CSH601318%2C00806%2C00460%2C%s%2C03818%2CSH600016%2CSH600519%2C&_=1433833729982'}
    'yonghuzuheshuju': {'type':3, 'url':'http://xueqiu.com/cubes/list.json?user_id=%s&count=20&_=1433833730125'},
    'yonghuchoucang': {'type':3, 'url':'http://xueqiu.com/favorites.json?page=1&size=20&userid=%s&_=1433835043446'},
    'yonghuzhutie': {'type':3, 'url':'http://xueqiu.com/v4/statuses/user_timeline.json?user_id=%s&page=1&type=&_=1433835493317'},
    'yonghuguanzhu': {'type':3, 'url':'http://xueqiu.com/friendships/groups/members.json?page=1&uid=%s&gid=0&_=1433835700334'},
    'yonghufensi': {'type':3, 'url':'http://xueqiu.com/friendships/followers.json?pageNo=1&uid=%s&size=20&_=1433835829415'},
    # 通过设置size可以改变接受数量
    'zuheguanzhushu': {'type':4, 'url':'http://xueqiu.com/service/stockfollows?symbol=%s&_=1433834132680'},
    'zuhepinglunxinxi': {'type':4, 'url':'http://xueqiu.com/statuses/search.json?symbol=%s&page=1&count=20&comment=0'},
    'zuheshouyilvzoushi': {'type':4, 'url':'http://xueqiu.com/cubes/nav_daily/all.json?cube_symbol=%s'},
    'zuhecangweilishijilu': {'type':4, 'url':'http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=%s&count=20&page=1'},
    'meirilingzhangbankuai': {'type':5, 'url':'http://xueqiu.com/cubes/discover/industry/list.json?order=1&page=1&count=30'}
}

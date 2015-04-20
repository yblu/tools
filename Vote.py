#!/usr/bin/python
#coding:utf-8
import  http.cookiejar, urllib
from urllib.error import URLError, HTTPError
import json,time


#500次
#for i in range(1,500):
def vote(proxy):
    #投票页面url
    indexUrl="http://fafuglxy.com/index.jsp"
    #投票请求url
    voteUrl="http://fafuglxy.com/ajax/vote_h.jsp?cmd=voteItem"
    #投票请求参数
    parameters={
    "vid" : 8,
    "itemlist" : [1]
    }
    #cookie持有
    cj = http.cookiejar.CookieJar()
    enable_proxy = True  
    proxy_handler = urllib.request.ProxyHandler({"http" : proxy})  
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),proxy_handler)
    #proxy=urllib.request.ProxyHandler({'sock5':'183.207.228.9:80'})
    #opener.add_handler(proxy)
    urllib.request.install_opener(opener)
    req=urllib.request.Request(indexUrl)
    resp= urllib.request.urlopen(req)
    #print(resp.getheader("Set-Cookie"))
    #print(resp.getheaders())
    #print(cj)
    #设置参数
    parameters['userAgent']="Mozilla/5.0  sdsdsi (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) dsd Chrome/31.0.1650.63 Safari/537.36 SE 2.X MetaSr 1.0"
    parameterencode=urllib.parse.urlencode(parameters)
    #print(parameterencode)
    parameterencode=parameterencode.encode('UTF-8')
    #print(parameterencode)
    #request=urllib.request.Request(voteUrl,parameterencode)
    resp2= opener.open(voteUrl,parameterencode)
    #resp2= urllib.request.urlopen(voteUrl,parameterencode)
    print("请求完毕,{0}".format(resp2.status))
    jsonData = json.loads(resp2.read().decode('utf-8'))
    print(jsonData)
    time.sleep(3)

if __name__ == "__main__":
    proxy='113.142.37.248:80'
    vote(proxy)

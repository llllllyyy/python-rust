# coding=UTF-8
import urllib
import urllib2
import pymongo
import re
import requests
import time
import random
print int(random.random()*20)
# def mon():
#     client = pymongo.MongoClient('', 27017)
#     db = client.store
#     collection = db.skunew
#     return collection
# if __name__ == '__main__':
#  col=mon()
 # for i in col.find():
 #    print i
 #    i['pic']="https://xpayv3-file.oss-cn-hangzhou.aliyuncs.com/archive/e246fb4a-d4c3-11e7-871c-0242c0a80002.jpg"
 #    col.save(i)
# def getpic(str,str1):
#     url="https://search.jd.com/Search?keyword="+str+'+'+str1+"&enc=utf-8&pvid=653d1450f36141dfb2b4d808947b1b9a"
#     try:
#         req = urllib2.Request(url)
#         res_data = urllib2.urlopen(req, timeout=5)
#         res = res_data.read()
#         pattern1 = '<img width=.*?//(.*?)" />'
#         pattern = re.compile(pattern1)
#         m = pattern.search(res)
#         if m:
#          pic=m.group(1)
#          return pic
#     except IOError:
#         print "异常"
# if __name__ == '__main__':
#     x=0
#     conn=mon()
#     for i in conn.find():
#         name = i["name"].encode("utf-8")
#         if i['catagory']:
#             catagory = i['catagory'].encode("gbk")
#             pic="http://"+getpic(name,catagory)
#             print pic
#             urllib.urlretrieve(pic, 'tu.jpg')
#             x+=1
#

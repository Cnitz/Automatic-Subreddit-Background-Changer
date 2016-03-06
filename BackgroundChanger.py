#!/usr/bin/python
import urllib2
import urllib
import json
import httplib
import time
import subprocess
import os
import datetime
import config



timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

hdr= { 'User-Agent' : 'subreddit picture retrieval bot by me' }
conn = httplib.HTTPConnection('www.reddit.com')
name = config.subreddit['name']
conn.request('GET', '/r/'+name+"/.json?after=t3_10omtd/", headers=hdr)
data = json.loads(conn.getresponse().read())
conn.close()

url = data['data']['children'][0]['data']['url']

if url.find("imgur") > -1:
    if url.find(".png") == -1:
        if url.find(".jpg") == -1:
            url = url + ".png"



user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
r = urllib2.Request(url, headers=headers)
page = urllib2.urlopen(r).read()

os.system("rm *pic.png")

output = open(timestamp + "pic.png",'wb')
output.write(page)

dir = os.listdir(".")
pic = ""
for file in dir:
    if(file.find("pic.png") > -1):
        pic = file
       
realpath = os.path.abspath(pic)




cmd2 = "osascript -e 'tell application \"System Events\"\n" + "tell current desktop\n" + "set picture to POSIX file \"" + realpath + "\" as alias\n" + "end tell\n" + "end tell'"


os.system(cmd2)



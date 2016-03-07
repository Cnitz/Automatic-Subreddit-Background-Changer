#!/usr/bin/python
import urllib.request, urllib.parse, urllib.error
import json
import http.client
import time
import subprocess
import os
import datetime
import config
import ctypes
from PIL import Image


true = 1
false = 0
minWidth = config.minResolution['width']
minHeight = config.minResolution['height']

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

def setTime():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

def getPic():
    setTime()
    removePics()
    
    hdr= { 'User-Agent' : 'subreddit picture retrieval bot by me' }
    conn = http.client.HTTPConnection('www.reddit.com')
    name = config.subreddit['name']
    conn.request('GET', '/r/'+name+"/.json?after=t3_10omtd/", headers=hdr)
    data = json.loads(conn.getresponse().read().decode())
    conn.close()

    i = 0

    while true :
        while data['data']['children'][i]['data']['is_self'] == true :
            i = i + 1

        url = data['data']['children'][i]['data']['url']

        if url.find("imgur") > -1:
            if url.find(".png") == -1:
                if url.find(".jpg") == -1:
                    url = url + ".png"
        


        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }

        r = urllib.request.Request(url, headers=headers)
        page = urllib.request.urlopen(r).read()
        output = open(timestamp + "pic.png",'wb')
        output.write(page)
        if checkResolution(timestamp + "pic.png") == true :
            return
        i = i + 1
        

def checkResolution(filepath):
    im = Image.open(filepath)
    width, height = im.size
    if width < minWidth :
        return false
    if height < minHeight :
        return false
    return true

def removePics():
    dir = os.listdir(".")
    for file in dir:
        if(file.find("pic.png") > -1):
            os.remove(file)


removePics()
getPic()

dir = os.listdir(".")
pic = ""
for file in dir:
    if(file.find("pic.png") > -1):
        pic = file
       
realpath = os.path.abspath(pic)



SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(20, 0, realpath , 2)


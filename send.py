import requests
import sys
import urllib2

url="http://159.89.166.12:13500/"
done 	= "pctf{"
words	= open("md5.txt","rb").readlines()

for i in words:
	key 	= i.strip()
	cookies = {'flag': key }
	http 	= requests.post(url,cookies=cookies)
	content = http.content
	if done in content:
			print content
			break
	else:
			break


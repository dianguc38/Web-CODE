import hashlib
import re

for i in range(0,999999999):
md5 = hashlib.md5(str(i).encode('utf-8')).hexdigest()
regex = re.match("^[0-9]+$",md5[3:])
if ((md5[0:2] == '0e') and regex):
  print ("Found : Seed = 0e && hash = " + str(i) + " => " + md5)
  break
else:
  print ("Wrong with!!! : " + str(i))

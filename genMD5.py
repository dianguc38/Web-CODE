import hashlib
import string
import re
def generateMD5():
    pattern = "^0+e[0-9]+$"
    i = 214000000
    while True:
        if i % 1000000 == 0:
            print("i:" + str(i))
        s = '0e' + str(i)
        md5 = hashlib.md5(s.encode("utf-8")).hexdigest()
        m = re.search(pattern, md5)
        if m:
            print("source:", s)
            print("md5   :", md5)
            return s
        i = i + 1
if __name__ == "__main__":
    generateMD5()

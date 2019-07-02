import string

f_One = open("flag.txt","rb") # flag co san
str_One=f_One.read()
str_One=str_One.split("\r\n")

f_Two= open("addflag.txt","rb") #flag moi tu request
str_Two=f_Two.read()
str_Two=str_Two.split("\r\n")

f_Three = open("sortflag.txt","w") #flag sau khi sort

def sort(dictionary):
	sort = sorted(dictionary.items(), key= lambda t:t[1],reverse= True)
	length =len(sort)
	for num in range(length):
		#print sort[num][0]
		logFlag(sort[num][0])

def comPare(str_One,str_Two):
	count = 0
	dictionary = dict.fromkeys(str_One, "")
	for str_O in str_One:
		for str_T in str_Two: 
			str_O_split = list(str_O)
			str_T_split = list(str_T)			
			for i in range(20):
				if (str_O_split[i] == str_T_split[i]):
					count += 1
			dictionary[str_O] = count
			count = 0
	sort(dictionary)

def logFlag(flag):
	f_Three.write(flag + "\r\n")

if __name__ == '__main__':					
	comPare(str_One,str_Two)

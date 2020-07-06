def readList():
	nlist = []
	flag = True;
	while flag :
		number = int(input("숫자를 입력하시오: "))
		if number < 0:
			flag = False
		else :
			nlist.append(number)
	return nlist

def processList(nlist):
	nlist.sort()
	return nlist


def printList(nlist):
	for i in nlist:
		print("성적=", i)

def main():
	nlist = readList()
	processList(nlist)
	printList(nlist)

if __name__ == "__main__":
	main()

data = [ ]
f = open("C:\\workpy\\data.txt", "r")

# 파일에 저장된 모든 줄을 읽는다.
for line in f.readlines():
	# 줄바꿈 문자를 삭제한 후에 리스트에 추가한다. 
    data.append(line.strip())

print(data)

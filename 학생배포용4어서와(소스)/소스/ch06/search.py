def linearSearch(aList, key):
	for i in range(len(aList)):		# 리스트의 길이만큼 반복한다. 
		if key == aList[i]:			# 키가 발견되면 i를 반환하고 종료한다. 
			return i
	return -1				# 키가 발견되지 않고 반복이 종료되었으면 
						# -1을 반환한다. 

numbers = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]

position = linearSearch(numbers, 80)

if position != -1:
	print("탐색 성공 위치 =  ", position)
else:
	print("탐색 실패 ")

# 선택 정렬을 구현하는 함수
def selectionSort( aList ):

  for i in range( len( aList ) ):	# 리스트의 모든 요소에 대하여 반복
    least = i			# i번째 요소를 최소값이라고 가정
    leastValue = aList[i]

    for k in range( i + 1 , len( aList ) ):	# (i+1)번째 요소를 최소값이라고 가정
      if aList[k] < leastValue:		# k번째 요소가 현재의 최소값보다 작으면
        least = k				# k번째 요소를 최소값으로 한다.
        leastValue = aList[k]

    tmp = aList[i]				# i번째 요소와 최소값을 교환한다. 
    aList[i] = aList[least]
    aList[least] = tmp

list1 = [ 7, 9, 5, 1, 8 ]
selectionSort(list1)
print(list1)

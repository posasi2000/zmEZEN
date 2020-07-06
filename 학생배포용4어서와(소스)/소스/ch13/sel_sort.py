def selectionSort(alist):
   for i in range(len(alist)):
        minPos = getMinPos(alist, i)
        temp = alist[minPos]
        alist[minPos] = alist[i]
        alist[i] = temp

def getMinPos(alist, start):
    minPos = start
    for i in range(start+1, len(alist)):
        if alist[i] < alist[minPos]:
            minPos = i
    return minPos

alist = [1, 4, 5, 9, 8, 2, 7]
selectionSort(alist)
print(alist)

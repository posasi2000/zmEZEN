def insertionSort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j+1] = my_list[j]
            j = j - 1
        my_list[j + 1] = key

my_list = [5, 2, 4, 6, 1, 3]
insertionSort(my_list)
print(my_list)

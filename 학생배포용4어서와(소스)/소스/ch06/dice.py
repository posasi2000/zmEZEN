rows = 6
cols = 6
table = [ ]

# 2차원 리스트를 생성한다. 
for row in range(rows): 
	table += [[0]*cols]

# 2차원 리스트의 각 요소에 rows와 cols 값을 더하여 저장한다. 
for row in range(rows): 
    for col in range(cols): 
        table[row][col] = (row+1+col+1) 

print(table)

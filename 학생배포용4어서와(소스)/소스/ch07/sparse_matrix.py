matrix = {(1, 2): 1, (2, 2): 2, (3, 2): 3}
for y in range(5):
	for x in range(5):
		print(matrix.get((y, x), 0), end=" ")
	print()

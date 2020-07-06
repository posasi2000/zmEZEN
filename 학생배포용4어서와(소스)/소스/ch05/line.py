def get_line(x1, y1, x2, y2):
    if (x1 == x2):
        return 0, 0
    else:
        slope = (float)(y2 - y1) / (float)(x2 - x1)
        yintercept = y1 - slope*x1
        return slope, yintercept			# 2개의 값을 반환한다. 
    
x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
slope, yintercept = get_line(x1, y1, x2, y2)		# 반환된 값을 풀어서 변수에 저장한다.
print("기울기=", slope, "y절편=", yintercept)

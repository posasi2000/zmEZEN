p1x = int(input("첫번째 사각형의 P1.x="))
p1y = int(input("첫번째 사각형의 P1.y="))
p2x = int(input("첫번째 사각형의 P2.x="))
p2y = int(input("첫번째 사각형의 P2.y="))

p3x = int(input("두번째 사각형의 P3.x="))
p3y = int(input("두번째 사각형의 P3.y="))
p4x = int(input("두번째 사각형의 P4.x="))
p4y = int(input("두번째 사각형의 P4.y="))

overlapped = not( p4x < p2x or
    p3x > p2x or
    p2y < p3y or
    p1y > p4y)

if overlapped:
    print("두개의 사각형이 겹침!")
else:
    print("두개의 사각형이 겹치지 않음!")

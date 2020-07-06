def area(w, h):
	return w*h

def input_pos(msg):
    value = int(input(msg))
    while value <= 0:
        value = int(input('양수만 입력하시오: '))
    return value

width = input_pos('사각형의 가로: ')
height = input_pos('사각형의 세로: ')

print( '면적=', area(width, height))

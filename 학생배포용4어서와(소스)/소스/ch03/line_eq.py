x1 = int(input('첫 번째 점의 x좌표: '))
y1 = int(input('첫 번째 점의 y좌표: '))
x2 = int(input('두 번째 점의 x좌표: '))
y2 = int(input('두 번째 점의 y좌표: '))

if( (x2-x1)!= 0): 
	m = (y2-y1)/(x2-x1)
	q = y1-m*x1
	print('직선의 방정식은', m, 'x+', q)
else: 
	print('직선의 방정식은 x=', x1)

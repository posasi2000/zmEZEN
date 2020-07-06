from random import *
from math import sqrt

n = int(input("반복횟수를 입력하시오: "))	# n은 전체 점의 개수이다. 

inside=0
for i in range(0, n):
	x=random()			# random()은 0.0에서 1.0 사이의 난수를 반환한다. 
	y=random()
	if sqrt(x*x+y*y)<=1:	# 원점으로부터의 거리가 1.0이하이면 원안에 있는 점이다. 
		inside+=1
pi=4*inside/n
print( pi)

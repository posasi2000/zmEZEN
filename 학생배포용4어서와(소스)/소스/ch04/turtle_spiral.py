import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

size = 20
for i in range(30):		# 30번 반복한다.
   t.stamp()     			# 거북이 모양을 화면에 그린다.       
   size = size + 3   		# 전진하는 거리를 3만큼 증가시킨다. 
   t.forward(size)			# size 만큼 전진한다. 
   t.right(24)       			# 왼쪽으로 24도 회전한다. 

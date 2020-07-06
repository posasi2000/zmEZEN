import turtle

window = turtle.Screen()		# 화면 객체를 가져온다. 
window.bgcolor("lightgreen")	# 배경색을 녹색으로 변경한다.

t = turtle.Turtle()		# 터틀 객체를 변수 t에 저장한다. 
t.shape("turtle")			# 터틀 객체의 모습을 거북이로 변경한다.
t.color("blue")			# 터틀 객체의 색상을 파랑색으로 한다. 

# 리스트를 변수에 할당한다. 
colors = ["yellow", "red", "purple", "blue"]
for c in colors:			# 색상 리스트에 대하여 반복한다.
    t.color(c)			# 펜 색상을 변경한다. 
    t.forward(200)			# 200픽셀만큼 전진한다. 
    t.left(90)			# 왼쪽으로 90도 회전한다. 

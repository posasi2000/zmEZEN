import math
import turtle

t = turtle.Turtle()

t.pendown()				# 터틀 객체의 펜을 내린다. 
for angle in range(360):			# 360번 반복한다. 
    y = math.sin(math.radians(angle))	# angle 값에 대응되는 싸인값을 계산한다. 
    scaledX = angle			# x축의 좌표값을 각도로 한다. 
    scaledY = y * 100			# y축의 좌표값을 싸인값으로 한다. 
    t.goto (scaledX, scaledY)		# 터틀 객체를 (scaledX, scaledY)로 이동시킨다. 
t.penup()				# 터틀 객체의 펜을 올린다.

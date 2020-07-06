import math
 
def sphereVolume(radius):
    volume = (4.0 / 3.0) * math.pi * radius * radius * radius
    return volume;
 
radius = float(input('구의 반지름을 입력하시오: '))
print(sphereVolume(radius))

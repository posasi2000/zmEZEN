statements = '''
import math
def area_of_circle(radius):
	return math.pi * radius * radius
		
'''
exec(statements)
print(area_of_circle(5))


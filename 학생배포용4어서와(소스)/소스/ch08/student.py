class Student:
	def __init__(self, name=None, age=0):
		self.__name = name
		self.__age = age

obj=Student()
print(obj.__age)

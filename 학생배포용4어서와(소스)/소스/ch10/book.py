class Book:
	title = ''
	pages = 0

	def __init__(self, title='', pages=0):
		self.title = title
		self.pages = pages

	def __str__(self):
		return self.title

	def __add__(self, other):
		return self.pages + other.pages
book1 = Book('자료구조', 600)
book2 = Book('C언어', 700)
print(book1+book2)



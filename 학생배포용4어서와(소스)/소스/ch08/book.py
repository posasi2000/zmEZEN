class Book:
   def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages

   def __str__(self):
      return "제목:%s , 저자:%s, 페이지:%s " % \
              (self.title, self.author, self.pages)

   def __len__(self):
      return self.pages

book = Book("Data Structure", "Chun", 650)
print(book)
print(len(book))

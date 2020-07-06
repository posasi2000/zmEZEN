def addNumber(fixedNum):
  def add(number):
      return fixedNum + number
  return add

func = addNumber(10)
print(func(20))

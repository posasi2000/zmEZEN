# 함수가 정의된다.
def sub( mylist ):
   # 리스트가 함수로 전달된다. 
   mylist = [1, 2, 3, 4]   # 새로운 리스트가 매개변수로 할당된다. 
   print ("함수 내부에서의 mylist: ", mylist)
   return

# 여기서 sub() 함수를 호출한다. 
mylist = [10, 20, 30, 40];
sub( mylist );
print ("함수 외부에서의 mylist: ", mylist)

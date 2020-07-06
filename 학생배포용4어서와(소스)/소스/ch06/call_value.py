def func1(x):
    print( "x=",x," id=",id(x))
    x=42
    print( "x=",x," id=",id(x))

y = 10

print( "y=",y," id=",id(y))
func1(y)
print( "y=",y," id=",id(y))

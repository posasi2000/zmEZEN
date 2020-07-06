table ={0:0, 1:1}

def fib(n):
    if n not in table:
        value=fib(n-1)+fib(n-2)
        table[n]=value
    return table[n]

print(fib(100))

# 피보나치 수열 모듈

def fib(n):    # 피보나치 수열을 화면에 출력한다. 
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


fib(5)
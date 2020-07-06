# while 문을 이용한 최대 공약수 구하기 프로그램
x = int(input("정수를 입력하시오(큰수): "))
y = int(input("정수를 입력하시오(작은수): "))

while (y != 0):
    r = x % y
    x, y = y, r
print("최대 공약수는 %d입니다." % x)

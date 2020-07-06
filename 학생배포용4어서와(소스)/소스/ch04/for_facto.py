
# 반복을 이용한 팩토리얼 구하기
fact=1.0
n = int(input("정수를 입력하시오:  "))

for i in range(1, n+1) :
    fact = fact * i;

print(n,"!은",  fact, "이다.")

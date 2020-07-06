# while 문을 이용한 성적의 평균 구하기 프로그램
# 필요한 변수들을 초기화한다.
n = 0
sum = 0
score = 0

print("종료하려면 음수를 입력하시오")
# grade가 0이상이면 반복
# 성적을 입력받아서 합계를 구하고 학생 수를 센다.
while score >= 0 :
    score = int(input("성적을 입력하시오: "))
    if score > 0:
        sum = sum + score
        n = n + 1

# 평균을 계산하고 화면에 출력한다.
if n > 0 :
	average = sum / n
print("성적의 평균은 %f입니다." % average)

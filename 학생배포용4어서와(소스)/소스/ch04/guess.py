import random

tries = 0
number = random.randint(1, 100)
print('number=', number)

print("1부터 100 사이의 숫자를 맞추시오")

while tries < 10:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < number:
        print("낮음!")
    elif guess > number:
        print("높음!")
    else:
        break

if guess == number:
     print("축하합니다. 시도횟수=", tries)
else:
     print("정답은 ", number)

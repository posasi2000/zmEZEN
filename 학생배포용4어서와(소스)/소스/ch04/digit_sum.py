number = 12345
sum = 0;
while number > 0 :
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("자리수의 합은 %d입니다." % sum)

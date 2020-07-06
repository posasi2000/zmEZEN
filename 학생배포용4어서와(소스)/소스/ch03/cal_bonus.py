mySale = int(input("실적을 입력하시오(단위: 만원): "))

if (mySale >= 1000) :
	result = "실적 달성"
	bonus = (mySale - 1000) / 10
else :
	result = "실적 달성 못함"
	bonus = 0
print(result, "보너스: ", bonus)

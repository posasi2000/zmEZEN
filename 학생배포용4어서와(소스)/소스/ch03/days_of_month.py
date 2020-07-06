month =int(input("월을 입력하시오: "))
if (month==2): 
	print("월의 날수는 29일")
elif (month==4 or month==6 or month==10): 
	print("월의 날수는 30일")
else :
	print("월의 날수는 31일")

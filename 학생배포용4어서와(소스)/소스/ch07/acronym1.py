phrase  = input("문자열을 입력하시오: ")
  
acronym = ""
for word in phrase.upper().split():
	acronym += word[0]
  
print( acronym )

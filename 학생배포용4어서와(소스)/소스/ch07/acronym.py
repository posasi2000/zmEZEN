'''
아크로님 (아크라님, acronym)
원뜻은 머리 글자의 뜻. 아크라님이라고도 한다
두문자어 (Acronym, 頭字語)
두문자어(頭文字語)는 낱말의 머리글자를 모아서 만든 준말이다.
'''

table = { "B4": "Before",
          "TX": "Thanks",
          "BBL": "Be Back Later",
          "BCNU":"Be Seeing You",
          "HAND":"Have A Nice Day" }

message = input('번역할 문장을 입력하시오: ')
words = message.split()
result = ""
for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word

print(result)

statement = input("문자열을 입력하시오: ")

alphas = 0
digits = 0
spaces = 0

for c in statement:
   if c.isalpha():
      alphas = alphas + 1
   if c.isdigit():
      digits = digits + 1
   if c.isspace():
      spaces = spaces + 1

print ("알파벳 문자의 개수=", alphas)
print ("숫자 문자의 개수=", digits)
print ("스페이스  문자의 개수=", spaces)

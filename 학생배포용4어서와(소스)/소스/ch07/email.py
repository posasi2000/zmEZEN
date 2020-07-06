address=input('이메일 주소를 입력하시오: ')

(id, domain) = address.split('@')

print(address)
print('     '+id)
print('     '+domain)

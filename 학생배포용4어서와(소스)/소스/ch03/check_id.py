user_list =['김철수', '홍길동', '김영희']

name=input('아이디: ')
if name in user_list:
    password = input('패스워드를 입력하시오: ')
    if password == '12345678':
        print('환영합니다.')
    else:
        print('잘못된 패스워드입니다. ')
else :
    print('알 수 없는 사용자입니다!')

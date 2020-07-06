credits = float(input('이수한 학점수를 입력하시오: '))
gpa = float(input('평점을 입력하시오: '))
if credits >= 140 and gpa >=2.0:
    print('졸업 가능합니다!')
else:
    print('졸업이 힘듭니다!')

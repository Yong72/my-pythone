#성적을 기반한 합격, 불합격 구분
for i in range (1, 6):
    iMArk1 = eval (input('성적을 입력하세요 :: '))
    if iMArk1 >= 60: 
        print("%d번 학생은 합격입니다." % i)
    else: 
        print("%d번 학생은 불합격입니다." % i)
        
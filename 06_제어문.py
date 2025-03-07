for i in range(1, 6):
    print("{0}번째 반복: {1}".format(i, i * 10))

for i in range(1, 6):
    print(f"숫자: {i}")

for i in range(1, 6):
    print(f"{i}의 제곱값은 {i**2}")

for i in range(1, 6):
    print(f"현재 숫자: {i:02d}")  # 두 자리 숫자로 맞춤 (01, 02, 03...)

names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names, 1):
    print(f"{i}번째 이름: {name}")

# While문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
# 조건이 만족되는 동안 넘어감.
# 명함 관리 프로그램 작성
# 1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
# 명함에는 1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교를 적으면 됩니다.
# 

display = '''
--------------------------------------------------------------
1. 명함 입력 2. 명함 수정 3. 명함 삭제 4. 명함 목록 보기 5. 종료
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''
card_display = '''
--------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''
card_display2 = '''
--------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교, 5. 전체 삭제
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

menu = ''
card_list = []
list = []
while menu != '5':
    print(display)
    menu = int(input())

    if menu == 1 :
        name = input('이름 입력 >')
        email = input('이메일 주소 입력 >')
        tel = input('전화번호 입력 >')
        belong = input ('직장 또는 학교 입력 >')
        list = [name,email,tel,belong]
        print("명함이 입력되었습니다", list)

    elif menu == 2 :
        print(card_display)
        number = int(input())
        if number == 1 :
            list[0] = input('수정할 이름 입력>')
        if number == 2 :
            list[1] = input('수정할 이메일 주소 입력 >')
        if number == 3 :
            list[2] = input('수정할 전화번호 입력 >')
        if number == 4 :
            list[3] = input('수정할 직장 또는 학교 입력 >')
        print("명함이 수정되었습니다", list)

    elif menu == 3 :
        print(card_display)
        number = int(input())
        if number == 1 :
            del list[0]
        if number == 2 :
            del list[1]
        if number == 3 :
            del list[2]
        if number == 4 :
            del list[3]
        if number == 5 :
            del list
        print("명함이 삭제되었습니다", list)

    elif menu == 4 :
        print(card_list)

    elif menu == 5 :
        print('프로그램 종료')
        sys.exit()
    else :
        print("메뉴 선택을 잘못하셨습니다.")
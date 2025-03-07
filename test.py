# 조건이 만족되는 동안 넘어감.
# 명함 관리 프로그램 작성
# 1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
# 명함은 리스트로 1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교를 적으면 됩니다.
# 명함 목록이란 여러명의 명함을 담은 리스트입니다.
import sys

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
        card_list.append(list)
        list.insert(0,card_list.index(list)+1)
        print("명함이 입력되었습니다", list)

    elif menu == 2 :
        print(card_display)
        list_num = input('수정할 명함의 번호 입력 >')
        number = int(input('수정할 부분 번호 입력 >'))
        if number == 1 :
            card_list[int(list_num)-1][0] = input('수정할 이름 입력>')
        if number == 2 :
            card_list[int(list_num)-1][1] = input('수정할 이메일 주소 입력 >')
        if number == 3 :
            card_list[int(list_num)-1][2] = input('수정할 전화번호 입력 >')
        if number == 4 :
            card_list[int(list_num)-1][3] = input('수정할 직장 또는 학교 입력 >')
        
        print("명함이 수정되었습니다", card_list[int(list_num)-1])

    elif menu == 3 :
        print(card_display2)
        list_num = input('삭제할 명함의 번호 입력 >')
        number = int(input('삭제할 부분 번호 입력 >'))
        if number == 1 :
            del card_list[int(list_num)-1][0]
        if number == 2 :
            del ard_list[int(list_num)-1][1]
        if number == 3 :
            del ard_list[int(list_num)-1][2]
        if number == 4 :
            del ard_list[int(list_num)-1][3]
        if number == 5 :
            del card_list[int(list_num)-1]
        
        print("명함이 삭제되었습니다", card_list)
    elif menu == 4 :
        print(card_list)

    elif menu == 5 :
        print('프로그램 종료')
        sys.exit()
    else :
        print("메뉴 선택을 잘못하셨습니다.")

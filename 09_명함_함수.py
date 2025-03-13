## 명함관리 프로그램 작성
# 1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록보기, 5.종료

import sys
import namecard_func as ncf

display = '''
-------------------------------------------------------------
1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록보기, 5.종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

card_list=[['홍길동', '111-222-3333', '부산', 'hong@gmail.com'], ['박나리', '22-4444-7777', '서울', 'park@gmail.com']]
menu = ''
while True:
  menu = input(display)
  if menu == '1':
    print('명함입력')
    card_list = ncf.card_input(card_list)
  elif menu == '2':
    print('명함수정')
    card_list = ncf.card_update(card_list)

  elif menu == '3':
    print('명함삭제')
    card_list = ncf.card_delete(card_list)

  elif menu == '4':
    print('명함목록보기')
    card_list = ncf.card_show(card_list)
    
  elif menu =='5':
    print('프로그램 종료')
    sys.exit()
  else:
    print('메뉴선택을 잘못하셨습니다.')
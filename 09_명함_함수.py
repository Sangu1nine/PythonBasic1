## 명함�?�? ?��로그?�� ?��?��
# 1.명함?��?��, 2.명함?��?��, 3.명함?��?��, 4.명함목록보기, 5.종료

import sys
import namecard_func as ncf
filename = 'namecard.json'

display = '''
-------------------------------------------------------------
1.명함?��?��, 2.명함?��?��, 3.명함?��?��, 4.명함목록보기, 5.종료
-------------------------------------------------------------
메뉴�? ?��?��?��?��?�� >>> '''

card_list = ncf.card_load(filename)
menu = ''
while True:
  menu = input(display)
  if menu == '1':
    print('명함?��?��')
    card_list = ncf.card_input(card_list)
  elif menu == '2':
    print('명함?��?��')
    card_list = ncf.card_update(card_list)

  elif menu == '3':
    print('명함?��?��')
    card_list = ncf.card_delete(card_list)

  elif menu == '4':
    print('명함목록보기')
    card_list = ncf.card_show(card_list)
    
  elif menu =='5':
    print('?��로그?�� 종료')
    ncf.card_save(card_list,filename)
    sys.exit()
  else:
    print('메뉴?��?��?�� ?��못하?��?��?��?��.')
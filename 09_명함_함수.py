## ëª…í•¨ê´?ë¦? ?”„ë¡œê·¸?¨ ?‘?„±
# 1.ëª…í•¨?…? ¥, 2.ëª…í•¨?ˆ˜? •, 3.ëª…í•¨?‚­? œ, 4.ëª…í•¨ëª©ë¡ë³´ê¸°, 5.ì¢…ë£Œ

import sys
import namecard_func as ncf
filename = 'namecard.json'

display = '''
-------------------------------------------------------------
1.ëª…í•¨?…? ¥, 2.ëª…í•¨?ˆ˜? •, 3.ëª…í•¨?‚­? œ, 4.ëª…í•¨ëª©ë¡ë³´ê¸°, 5.ì¢…ë£Œ
-------------------------------------------------------------
ë©”ë‰´ë¥? ?„ ?ƒ?•˜?„¸?š” >>> '''

card_list = ncf.card_load(filename)
menu = ''
while True:
  menu = input(display)
  if menu == '1':
    print('ëª…í•¨?…? ¥')
    card_list = ncf.card_input(card_list)
  elif menu == '2':
    print('ëª…í•¨?ˆ˜? •')
    card_list = ncf.card_update(card_list)

  elif menu == '3':
    print('ëª…í•¨?‚­? œ')
    card_list = ncf.card_delete(card_list)

  elif menu == '4':
    print('ëª…í•¨ëª©ë¡ë³´ê¸°')
    card_list = ncf.card_show(card_list)
    
  elif menu =='5':
    print('?”„ë¡œê·¸?¨ ì¢…ë£Œ')
    ncf.card_save(card_list,filename)
    sys.exit()
  else:
    print('ë©”ë‰´?„ ?ƒ?„ ?˜ëª»í•˜?…¨?Šµ?‹ˆ?‹¤.')
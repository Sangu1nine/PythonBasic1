## λͺν¨κ΄?λ¦? ?λ‘κ·Έ?¨ ??±
# 1.λͺν¨?? ₯, 2.λͺν¨?? , 3.λͺν¨?­? , 4.λͺν¨λͺ©λ‘λ³΄κΈ°, 5.μ’λ£

import sys
import namecard_func as ncf
filename = 'namecard.json'

display = '''
-------------------------------------------------------------
1.λͺν¨?? ₯, 2.λͺν¨?? , 3.λͺν¨?­? , 4.λͺν¨λͺ©λ‘λ³΄κΈ°, 5.μ’λ£
-------------------------------------------------------------
λ©λ΄λ₯? ? ???Έ? >>> '''

card_list = ncf.card_load(filename)
menu = ''
while True:
  menu = input(display)
  if menu == '1':
    print('λͺν¨?? ₯')
    card_list = ncf.card_input(card_list)
  elif menu == '2':
    print('λͺν¨?? ')
    card_list = ncf.card_update(card_list)

  elif menu == '3':
    print('λͺν¨?­? ')
    card_list = ncf.card_delete(card_list)

  elif menu == '4':
    print('λͺν¨λͺ©λ‘λ³΄κΈ°')
    card_list = ncf.card_show(card_list)
    
  elif menu =='5':
    print('?λ‘κ·Έ?¨ μ’λ£')
    ncf.card_save(card_list,filename)
    sys.exit()
  else:
    print('λ©λ΄? ?? ?λͺ»ν?¨?΅??€.')
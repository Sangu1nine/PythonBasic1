import json

def card_input(card_list) :
    name = input('이름 >>> ')
    tel = input('전화번호 >>> ')
    address = input('주소 >>> ')
    while True:
        email = input('이메일 >>> ')
        check = 0
        for index in range(len(card_list)):
    # for index,card in enumerate(card_list):
            if card_list[index][3] == email:
                check = 1
                break
        if check == 0:
            break
    card_list.append([name,tel,address,email])
    print(card_list)
    return card_list

def card_update(card_list) :
    email = input('수정할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(card_list)):
        if card_list[index][3] == email:
            check = 1
        while True:
            item = input('수정할 항목을 선택하세요(1.이름, 2.전화번호, 3.주소,  4.종료)')
            if item == '4':
                break
            item = int(item)
            if item in (1,2,3):         
                card_list[index][item-1] = input('수정할 값을 입력 >>> ')
        if check == 0:
            print('데이터가 없습니다.')
    return card_list

def card_delete(card_list) :
    email = input('삭제할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(card_list)):
        if card_list[index][3] == email:
            check = 1
            print('삭제 >>> ', card_list.pop(index))
            break
    if check == 0:
        print('데이터가 없습니다.')
    return card_list

def card_show(card_list) :
    print('=' * 55)
    for card in card_list:
        print(f'{card[0]:10} {card[1]:15} {card[2]:10} {card[3]:10}')
    print('=' * 55)

def card_save(card_list,filename) :
    with open(filename, 'w',encoding="utf-8") as f :
        json.dump(card_list, f, indent=4,ensure_ascii=False)
    
def card_load(filename) :
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
    # return card_list
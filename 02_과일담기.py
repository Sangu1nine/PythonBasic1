# 과일을 받아서 박스에 담고 싶습니다.
# 박스에 담겨지는 과일의 개수는 과일마다 다릅니다.
# 과일의 개수를 받고, 박스에 몇개 담기는지 입력을 받고
# 박스에 담아서 몇 박스 몇 개인지 알려주는 프로그램을 작성
# 변수 : 과일의 개수, 박스당 몇개
# 값을 읿력 받아야 함 : input()
# 갑 데이터 타입 변환 (문자 -> 숫자)

fruit_a = input("과일a의 총 개수 >")
fruit_b = input("과일b의 총 개수 >")
fruit_c = input("과일c의 총 개수 >")
fnum_a = int(fruit_a)
fnum_b = int(fruit_b)
fnum_c = int(fruit_c)
box_a = input("박스a는 몇개입니까? >")
box_b = input("박스b는 몇개입니까? >")
box_c = input("박스c는 몇개입니까? >")
bnum_a = int(box_a)
bnum_b = int(box_b)
bnum_c = int(box_c)

print("하나의 a박스에는", fnum_a//bnum_a, "개의 과일이 들어가고", fnum_a%bnum_a, "개가 남습니다.")
print("하나의 b박스에는", fnum_b//bnum_b, "개의 과일이 들어가고", fnum_b%bnum_b, "개가 남습니다.")
print("하나의 c박스에는", fnum_c//bnum_c, "개의 과일이 들어가고", fnum_c%bnum_c, "개가 남습니다.")
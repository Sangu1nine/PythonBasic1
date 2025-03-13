def add(a,b) :
    return a + b

def sub(a,b) :
    return a - b

def mul(a,b) :
    return a * b

def indata() :
    a = int(input('입력:'))
    return a
#data1 = indata()
#data2 = indata()
# print(sub(data1,data2))

#def 함수_이름(*매개변수):
#    수행할_문장
#    ...
#    -> 값들을 리스트 형태로 저장함.

def add_many(*args) :
    print(type(args))
    result = 0
    for i in args :
        result += i
    return result
print(add_many(1,2,3,4.5,5,6,7,8,9))
print(type(add_many(1,2,3,4,5.5,6,7,8,9)))

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a = 1)

def item_print(**items) :
    print(type(items))

item_print(a = 'hong', b = 22)

list = []
def add_and_mul(a,b): 
    return a+b, a*b, a, b
print(add_and_mul(3,4))
print(len(add_and_mul(3,4)))
for i in range(1,len(add_and_mul(3,4))+1) :
    list.append(add_and_mul(3,4)[i-1])
print(list)

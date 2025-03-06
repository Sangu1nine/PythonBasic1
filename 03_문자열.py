text01 = "문자열"
text02 = '문자열'
text03 = "Hyunjun's"
text04 = ' "Hyunjun" is'
print(text01)
print(text02)
print(text03)
print(text04)

text05 = "첫 번째 줄\n두 번째 줄"
text06 = '''첫 번째
두 번째
세 번째'''
print(text05)
print(text06)
'''
실행하지 않을 건데
여러줄에 걸쳐서
설명하고 싶으면
'''
#위의 방식은 주석처리가 아니라 여러 줄 문자열 쓰기인데, print 명령이 없어서 그냥 씹히는 것.



text07 = '그는 \"지피지기면 백전백승\"이라고 말했다.'
print(text07)

# \n	문자열 안에서 줄을 바꿀 때 사용
# \t	문자열 사이에 탭 간격을 줄 때 사용
# \\	\를 그대로 표현할 때 사용
# \'	작은따옴표(')를 그대로 표현할 때 사용
# \"	큰따옴표(")를 그대로 표현할 때 사용

print(text01 + text06) 
# 문자열 2개를 이어 붙임
# str 과 int/float은 연산이 안됨!
print(text04 * 2) 
# 곱하기는 앞의 문자를 몇번 반복할 지
# ============= 로 줄 만들 때, = * 50 로 가능!

print(len(text04))
# 공백을 포함하여 개수를 셈


a = "Life is too short, You need Python"
print(a[3]) # 인덱스 값의 시작은 0
print(a[-1]) # 마지막 인덱스를 -1부터 반대로 셀 수도 있다.

print(a[0:4])
b = a[0:18]+a[22:]
print(b)

# Pithon -> Python
'''
a = "Pithon"
a[1] = 'y'
'''
# 위 방법은 str이 변경 불가능하기 때문에 불가능하다.
#되는 방법
a = "Pithon"
a[:1]
'P'
a[2:]
'thon'
a[:1] + 'y' + a[2:]
'Python'

# %d ~ % 정수 : 정수 대입
# %s % 문자 : 문자 대입
data1 = "I eat %d apples."
print(data1 % 3)



# format 함수를 사용한 포매팅

print("I eat {0} apples".format(3))

# f 문자열 포매팅
txt01 = "I eat {0} apples {1}"
print(txt01.format(3,'gggg'))
# 클래스(str)에 내장된 매서드를 부를 때는 클래스.함수()으로 시작한다.
# 매서드와 함수의 차이점 : 매서드는 항상 첫 번째 매개변수로 self를 받는다.
# format()은 args와 kwargs가 필수이다.


# 정렬
# 왼쪽 정렬
txt02 = "I eat {:<20} apples {}"
print(txt02.format(3,text03))
#가운데 정렬
txt03 = "I eat {:^10} apples {}"
print(txt03.format(3,text03))
#소수점 표현
txt04 = "I eat {:.2f} apples {}"
print(txt04.format(3,text03))
# 콤마
txt05 = "I eat {:,} apples {}"
print(txt05.format(3000000,text03))

# f '문자열' => 더 간단한 방법
name = "홍길동"
age = 24
txt07 = f'나의 이름은 {name:20}입니다. 나이는 {age:.2f}입니다.'
print(txt07)
# :20 에서 숫자 = 오른쪽 정렬, 문자 = 왼쪽 정렬


# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy"
str2 = 'Niceman'
str3 = ''
str4 = str('ace')
print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do tou have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String *중요
raw_S1 = r'C:\Programs\Test\Bin'
print(raw_S1)
raw_S2 = r"\\a\\a"
print(raw_S2)

# 멀티라인 '\' 을 안쓰면 에러!
multi = \
""" 
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4)    # 문자열을 순회하면서 'a'가 있는지 확인(결과는 Boolean)

# 문자열 형 변환
print(str(77) + 'a')    # 77을 string으로 보기때문에 결과는 77a
print(str(10.4))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'
#
# print(a.islower())    # a가 모두 소문자이면 True, 하나라도 대문자가있다면 False
# print(a.endswith('s'))    # a의 끝 글자가 's'라면 True, 아니라면 False
# print(a.capitalize())     # 첫글자를 대문자로 변환
# print(a.replace('nice', 'good'))    # nice를 good으로 변환
# print(list(reversed(b)))

a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])









# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
  "name": "Kim",
  "age": 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {3, 5, 7}

print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999
big_int2 = 7777777777777777777777777777
f1 = 1.234
f2 = 3.785
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)
print(int(result2))
print(float(c))
print(complex(3))
print(int(False))
print(int(True))
print(int('3'))
print(complex(False))



y = 100
y += 100
print(y)


# 수치 연산 함수
# https://docs.python.org/3/library/math.html
print(abs(-7))

n, m = divmod(100, 8) # 100을 8로 나눠서 몫은 n으로, 나머지는 m으로!
print(n, m)


import math

print(math.ceil(5.1))   # 5.1 보다 큰 가장 작은 정수
print(math.floor(3.874))    # 3.874 보다 가장 작은 정수






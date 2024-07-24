# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB
# 선언
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 980320}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

# 출력
print(a['name'])    # 'name'이라는 key가 없으면 바로 에러!
print(a.get('name'))
print(a.get('address'))     # 'address'라는 Key가 없어도 에러는 안나고 None으로 출력! 위의 'a['name'] 방법보다 더 선호
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

# Keys, values, items

# Keys
print(a.keys())
# print(a.keys()[0])   위의 출력결과가 리스트 처럼 생겨도 인덱스로 못 가져옴 따라서 하단의 방법으로 형변환 필수
print(list(a.keys()))
temp = list(a.keys())
print(temp[1:3])

# values
print(a.values())
print(list(a.values()))

# items
print(list(a.items()))    # 리스트 안에 튜플 형태

print(2 in b)
print('name2' not in a)



# 집합(set) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)      # 중복인 6이 하나가 없어짐   {1, 4, 5, 6}

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s2.union(s2))   # 교집합

print(s1 - s2)
print(s1.difference(s2))  # 차집합

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))





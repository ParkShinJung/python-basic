# Section02-1
# 파이썬 기초 코딩
# print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2024', '07', '23', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome to', end='')
print('the black parade', end='')
print('piano notes')

print()

# format 사용 [], {}. ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('Eunki', 7))

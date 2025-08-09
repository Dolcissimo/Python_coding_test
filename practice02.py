"""

대소문자 바꿔서 출력하기

"""

str = input("문자를 입력하세요: ")
a=''

for i in str:
    if (i.islower()):
        a += i.upper()
    else:
        a += i.lower()


print(a)

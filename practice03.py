"""
a, b 가 입력 되었을때
예시와 같은 형태로 출력하는 코드

입력 예시
4 5
출력 예시
a = 4
b = 5
"""

a , b = map(int , input("숫자를 입력하시오: ").strip().split(' '))
print(f"a = {a}\nb = {b}")

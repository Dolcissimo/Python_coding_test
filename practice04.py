"""
정수 l,r이 주어졌을 때, l이상 r이하 정수중
숫자 0,5로만 이루어진 모든 정수를 오름차순으로 저장한 배열을
return하는 함수
"""


def solution(l,r):
    answer = []
    for x in range (l,r+1):
        if set(str(x) <= {'0','5'}):
            answer.append(x)
        return answer if answer else [-1]

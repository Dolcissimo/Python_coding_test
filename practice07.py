"""
길이가 같은 문자열 str1 과 str2를 번갈아 출력하는 코드
"""

def solution (str1,str2):
    answer = ''.join(str1[i]+str2[i] for i in range(len(str1)))
    return answer

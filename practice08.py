"""
정수 리스트 unm_list가 주어질 때,
모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1
크면 0 return 하는 함수
"""

def solution(num_list):
    answer1,answer2 =1,0
    for i in range (len(num_list)):
        answer1 *= num_list[i]
        answer2 += num_list[i]

    return 1 if answer1 < answer2**2 else 0

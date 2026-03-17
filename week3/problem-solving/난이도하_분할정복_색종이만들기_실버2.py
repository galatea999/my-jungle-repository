# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
"""
마지막에 어려웠던 포인트 쓰기

Constraint
2 <= N <= 2^7

Idea
재귀, 이중리스트, BaseCase는 숫자가 하나만 있을때 갯수 +1
재귀의 기준은 로그 자르고 확인, 자르고 확인
문제는 이중 리스트로 어떻게 구현할 것인가

Complexity 
잘 모르겠음

Code

어려웠던 포인트 : 
"""

side_length = int(input())

#인풋 어떻게 받을건지만 정하면 끝날 것 같은데.. 

#한 줄씩 받아보죠 뭐. 두줄씩 받았을 때와 차이는?
paper = []
for i in range(side_length) :
    paper.append(input())


def divide(start_row, start_column, size) :
    1)


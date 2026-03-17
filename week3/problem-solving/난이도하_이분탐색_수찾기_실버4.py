# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

"""
Constraint 
N과 M이 주어지고, 10^5 안.
시간제한 1초. O(n^2)은 안됨, 그 아래는 괜찮을듯

idea 
이분탐색이니까 어떤 식으로든 정렬을 해놓고 (뭐 버블정렬, 삽입정렬 뭐든)
이분탐색 하면 될듯
1) 정렬하기 : 근데 정렬은 보통 n^2 아닌가? nlogn인 퀵정렬로 해보자.
2) 탐색하기 

Complexity
퀵정렬 : n log n
이분탐색은 logN.
"""

n = int(input())
target_list = map(int, input().split())
m = int(input())
compare_list = map(int, input().split())

def quick_sort(arr) :

def helper(arr,low,high) :

def 


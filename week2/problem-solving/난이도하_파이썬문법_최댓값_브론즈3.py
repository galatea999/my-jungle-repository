# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


max = 0
max_index = 0
for i in range(9) : 
    num = int(input())
    if num > max :
        max = num
        max_index = i+1

print(max)
print(max_index)
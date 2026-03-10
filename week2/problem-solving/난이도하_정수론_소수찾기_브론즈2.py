# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

num = int(input())

list = input().split()
#소수를 어떻게 판별할 것인가? 소수란? 나누어지는 수가 1과 자신밖에 없는 수. 약수가 2개인 수.
# 그 말은? 합성수가 아닌 수. 
result = 0 
for i in range(num) : #총 num개를 판별
    if int(list[i]) == 0 or int(list[i]) == 1 : 
        continue
    for j in range(int(list[i])-1, 1, -1) :
        if int(list[i]) % j == 0 :
            break #이러면 소수가 아님. for문에서 탈출
    else : 
        result += 1

print(result)
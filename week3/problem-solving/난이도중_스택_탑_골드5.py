# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

# 클린 코드


"""
Constraint
N <= 5 * 10^5, 제한 시간 1.5초 
브루트 포스 불가능. O(n)까지 감당 가능.
"""

"""
Idea 
1) 첫번째 값은 무조건 0
2) 왼쪽부터 스택으로 쌓아서 비교하면 될듯?
3) result에 등록 하고 나면 stack으로 들어가기
4) 9가 나왔을 때, 5는 들어갈 수 있으나, 7이 나왔을때 pop해서 비교했을때 실패했다면 빼기.
=> 비교 실패한 값은 아예 stack에서 빼기.



Complexity
1. O(n^2).. 이러면 안될텐데. 줄일 수 있는 방법이 뭐가 없을까. 
"""

count = int(input())

tops = list(map(int, input().split()))
stack = [] # stack에 값과 인덱스를 함꼐 저장
result = [] #첫 번째 값은 무조건 0

for i in range(len(tops)) :
    
    #최초조건 먼저 설정
    if i == 0 :
        stack.append((tops[i], i))
        result.append(0)
        continue
    
    #스택이 존재할 때
    while stack :
      # 스택 끝의 값이 적을 때 => 뱉어내고 다음 것과 비교
        if stack[-1][0] < tops[i] :
            stack.pop()
            continue # 다음 반복으로
            
        # 값을 찾았을 때 
        if stack[-1][0] >= tops[i] :
            result.append(stack[-1][1]+1)
            stack.append((tops[i],i)) 
            break #반복문 자체를 탈출

    #스택을 모두 소모했을 때 
    if not stack : 
        stack.append((tops[i],i))
        result.append(0)
    
    
print(' '.join(list(map(str, result))))

"""


# 더 시간 복잡도가 좋은 방법이 없을까? 여기서 for문을 두번 돌면 시간초과가 뜰텐데.
# while tops :
    
#     #최소 케이스
#     if len(tops) == 1 :
#         result.append(0)
#         break

#     tmp = tops.pop()

#     for i in range(len(tops)-1, -1, -1) :
#         if tops[i] >= tmp :
#             result.append(i+1)
#             break
        
#     else : #break 없이 끝날때만 실행되려면 for랑 같은 층위로 else를 써야함 
#         result.append(0)
        

        
# print(' '.join(map(str, result[::-1]))) 

#List comprehension으로도 써 보기


Test Case 
최소케이스 : 1에 탑이 하나일떄
연속명령 : 3 3 3 3 3 일때

"""
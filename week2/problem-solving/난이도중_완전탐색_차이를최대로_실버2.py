# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

"""
절댓값? 완전탐색? 결과를 하나하나 비교?

일단 절댓값 식을 구현해보자.

덧셈의 최댓값은, 결국 큰거에서 작은걸 빼면 되지 않나. 
그러면, 내림차순으로 정리를 해서 포인터가 양쪽에서 가운데로 오게 하면 되지 않나! 
그러나, 여기 절댓값이 씌이면? 
그러면 1) 정렬
2) 

Brute Force : 그냥 다 해보는 것. 결과를 비교를 해야하는가?
무식하게 직접 다 해 본다고 생각하자. 
최댓값을 출력하는 것이므로 for문을 돌면서 가장 큰 값이 나오면 그걸 저장하고 마지막에 출력하면 됨
그러면 n!의 문제잖아.
"""

def absolute (a,b) :
    if a>=b :
        return a - b
    else : 
        return abs(b-a)
    
def sort_and_some(nums) : #[20, 1, 15, 8, 4, 10] 
    

    def recursion(depth, path) :
        
        # Base case : 갯수만큼 모두 찾았을때 재귀를 끝내고 계산
       if len(path) == len(nums) :
           #currnet_list = [20, 1, 15, 8, 4, 10]
           #계산
           for i in range(path-1) :
              result += absolute(int(path[i]), int(path[i+1]))
            
            #계산 후 나온 result가 크면 max 경신 후 어디로 가지? 
           if result > max :
               maximum = result
            
           return maximum

    
       for i in nums :
            path.append(i)
            recursion(, path) #recursion이 반복될때마다 한번씩 덜해야하는데
            path.pop() 
    
    recursion(0,0)
    print()
    return 

n = int(input())
target_list = input().split()

sort_and_some(target_list)




# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

"""
메인 아이디어는, n이 있을때, 몇 번을 반복해야 하느냐?

Constraint :  5* 10^5. O(n)까지만 가능, 어 시간 제한 2초면 2 * 10 ^7이구나.

idea
1) 큐로 구현
2) 홀수번째엔 빼내고, 짝수번째엔 다시 뒤로 보냄. 1개가 남을 때까지 반복함.

"""

from collections import deque

numbers = int(input())
queue = deque()

for i in range(numbers) :
    queue.append(i+1)

while len(queue) > 1 :
    queue.popleft()
    queue.append(queue.popleft())

print(queue[-1])
    
"""
Complexity: 2n정도 되는듯

Test case => 이 과정을 안 하고 제출 넣으면 틀린다! 
최소케이스 : 1일때. 보길 잘 했다. 해결 완료.
연속명령 : 연속은 없음 
"""
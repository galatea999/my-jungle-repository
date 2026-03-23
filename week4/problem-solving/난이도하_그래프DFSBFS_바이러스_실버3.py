# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

"""
이건 연결된 노드로 이어질때마다 바이러스 카운트 수를 하나씩 추가하면 되는 문제.

번호수는 딱히 상관 없고,
[[]] 이중리스트로 연결되어 있는 노드들을 표시하는 것,
[0] 으로 감염 여부 표시하는 것
queue에 넣고 빈칸이 없을때까지 pop하는 것. 이런 것들이 중요하겠네.
연결 시켜놓고, 1번 컴퓨터부터 시작하면 됨. 
"""
from collections import deque

computer_count = int(input())

node_count = int(input())

linked_computers = [[] for _ in range(computer_count)]

is_infected = [0] * computer_count

infected_counter = 0

#노드를 연결시키는 과정
for _ in range(node_count) : #그냥 range(괄호) 숫자만큼 반복시키고 싶을때 변수명을 _로 써버림
    start, end = map(int, input().split()) #이렇게도 되는구나. 이게 왜 되지?
    linked_computers[start-1].append(end-1) #인덱스로 변환해주려면 -1을 해줘야함
    linked_computers[end-1].append(start-1) #왜 양방향이 되어야 하지? 직접 해 보자. 

#큐를 생성하고 1번 컴퓨터를 넣어줌 
queue = deque([0])
is_infected[0] = 1


while queue :
    current = queue.popleft()
    infected_counter += 1
    for vertex in linked_computers[current] :
        if not is_infected[vertex] :
            is_infected[vertex] +=1 
            queue.append(vertex)

print(infected_counter-1)
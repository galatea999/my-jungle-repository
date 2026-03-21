"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    #1. 결과 값으로 보낼 리스트와 탐색용으로 쓸 데큐 만듦
    visited = []
    will_visit = deque()

    # 2. 여정을 시작함 
    visited.append(start)
    will_visit.append(start)

    # 3. deque에는 앞으로 방문할 곳만 있어야함.
    #  지금 방문한 곳은 queue에서 뱉어서 방문중임
    
    #graph은 dict이므로, visiting을 key로 삼아 연결돼있는 것들을 순회
    #BFS이므로, 가까이 있는 것들부터 방문지로 삼음 => will_visit에 추가
    #!!! 다만, 이미 다녀온 곳은 가지 않음 => if not visited 조건 추가
    # visited 결과 값에도 넣음
    # !!! wii_visit deque가 빌때까지 반복
    
    while will_visit:
        visiting = will_visit.popleft()
        for vertex in graph[visiting] :
            if not vertex in visited :
                will_visit.append(vertex)
                visited.append(vertex)

    return visited
    

 

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


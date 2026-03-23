"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    #1. 주어진 관계로부터 그래프 그리기. 차수 또한 따로 생성. 위상정렬이라면 차수 변수는 따로 필요함
    graph = [[] for _ in range(vertices)]

    indegree = [0] * vertices

    for start, end in edges : 
        graph[start].append(end)
        indegree[end] += 1
    #2. queue를 만들고 차수가 0인것들 추가    
    queue = deque()
    result = []
    for i in range(vertices) :
        if indegree[i] == 0 : 
            queue.append(i) #차수가 0인것들을 추가 
    #3. queue에서 하나씩 뱉고, result에 추가하고, 인접 정점들의 차수를 빼고, 0인건 다시 queue로 추가
    while queue :
        currnet = queue.popleft()
        result.append(currnet)

        #인접 정점들에서 차수를 하나씩 빼고, 0인 놈은 queue로 추가
        for vertex in graph[currnet] : 
            indegree[vertex] -= 1
            if indegree[vertex] == 0 :
                queue.append(vertex) 
        

    
    return result
    
    """
    구조를 보자. 3단계 구조로 나눠서 보자.

    """
# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

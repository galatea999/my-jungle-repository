"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

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
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""

def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
# 깊이 우선 탐색을 만드려면 어떻게 해야할까. visited를 매개변수로 놓고 none으로 놓은건 
#순전히 재귀를 위한 장치. 이 아이디어를 잘 써먹으면 좋을듯. 내가 늘 힘들어하던 포인트 인듯
    if visited is None : 
        visited = [] #빈 리스트와 None은 엄연히 다름
    
    #일단 지금 방문했으니 visited에 추가해줌
    visited.append(start)

    for vertex in graph[start] :
        if not vertex in visited :
            dfs(graph, vertex, visited) #visited를 이렇게 실어보내면 초기화되지 않고 계속 결과가 쌓임
            #재귀함수를 쓸거면 이 함수의 output이 무엇인데?를 반드시 생각해야함.. 과정은 블랙박스로 치더라도.
    
    return visited #근데 그 visited가 dfs 들어갔다가 추가되어서 별거 안해도 이렇게 그냥 다시 돌아온다고?

"""
드디어 재귀 함수에서 결과값을 저장하는 방법의 미스테리가 풀렸다!
이런 식으로 매개변수에 visited를 넣으면 재귀에서도 결과값을 저장할 수 있음.
특히 처음에 조건을 visited = None으로 놓고, if visited None : visited = []로
조건부로 초기화해주면 visited가 재귀를 돌때마다 초기화되지 않을 뿐만 아니라,
같은 visited를 계속 공유하면서 참조하게 만들 수도 있음 (visited가 2개 3개 되는게 아님.. 감동)

그리고 이런 구조면 값들이 알아서 visited에 append 되고 있기 때문에 
return visited가 최초함수에서 결과값을 return해준다는데에서 의미가 있고,
나머지 재귀 안에서는 그 return값이 쓰이지는 않음. 해결 !!
"""


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")



"""

3.24 14:00
4주차 Weekly Quiz

1. 이진 탐색 트리의 시간 복잡도가 가장 나쁜 경우를 설명하고 이때 시간 복잡도를 제시하시오.

내 답 : 최악의 경우는 1,2,3,4,5 처럼 트리가 한 쪽으로 치우쳐 선형구조가 되는 경우이며, 이런 경우 O(n)이 된다.

2. 다음 인접 리스트 형태의 그래프에서 DFS의 방문 순서를 출력하시오. 시작 정점은 1임.
graph = {
  1: [2, 3],
  2: [4],
  3: [],
  4: []
}

내 답 : 1, 2, 4, 3

!!! 스택 기반 DFS면 [1,3,2,4]가 되고, 
재귀 DFS면 [1,2,4,3]이 됨! 둘 다 유효한 DFS임!



3.다음은 BFS를 구현한 코드이다. 빈칸에 들어갈 알맞은 코드를 작성하시오. 
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(__________)

내 답 : graph[node]

찾아본 결과 : extend는 iterable의 모든 객체를 추가
visited는 중복방지. 

4. DFS를 재귀가 아닌 스택을 이용해 구현하였다. 빈칸을 채워 코드를 완성하시오. 
graph = { 1: [2, 3], 2: [4], 3: [], 4: [] }
start = 1
visited = set()
stack = [start]
while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        ________________________________________

??? 근데 스택 방식과 재귀방식의 장단점이 뭐지? 
아 정리했었지. 스택은 공간에서 약점이 있고, 재귀는 시간에서 약점이 있음. 
??? 그리고 extend를 쓰네. 이게 더 좋은 방법이네. 난 어떻게 했었지? for문을 돌았나? !!!나는 for문을 돌아서 append했네. extend로 쓰자.
??? visited에도 add를 쓰네? append 안 쓰고 add를 쓰는건? set을 쓰는거랑 관련이 있겠지? 
!!! set을 쓰는게 성능이 훨씬 좋음. 
    if node not in visited를 돌 때, 노드 1000개를 탐색한다면 리스트는 1000번, set은 항상 1번임. 시간복잡도를 위한 선택임! in 함수, 아니 set이 Hash Table이기 때문에.

내 답 : stack.extend(graph[node])
??? 근데, DFS는 1,3,2,4나 1,2,4,3이나 상관이 없는건가?? !!! 위에 답해놨음. 재귀 기반과 같은 순서를 내고 싶으면, 출력을 reverse하면 됨
=> stack.extend(reversed(graph[node]))

5. 트리 구조가 컴퓨터 시스템에서 활용되는 예를 두 가지 제시하고, 각각 해당 구조가 적합하다고 생각하는 이유를 서술하시오.

내 답 : 잘 모르겠음. 컴퓨터 시스템에서 ..? 아직 공부를 못 했음... ! 

정답 : 
1) 파일 시스템 (디렉토리 구조) : 폴더 안에 폴더가 있는 구조가 그대로 트리이다. 부모-자식 관계가 명확하고, 경로 탐색이 루트에서 내려가는 방식.
2) DB 인덱스 (B-트리(?)) : DB에서 수백만건 중 원하는 값을 빠르게 찾기 위해 B-트리 인덱스를 사용. 매 단계마다 탐색 범위를 절반으로 줄이는 BST의 특성이 활용됨.

6. 아래 깊이 우선 탐색(DFS)의 예시를 참고하여 간선 방문 결과와 비트리(non-tree) 간선 목록을 리턴하는 파이썬 함수를 작성
하려고 한다. 아래 빈 곳을 채워 파이썬 함수를 완성하시오.
 참고로 각 빈 코드는 한줄 이상의 다중 코드가 될 수 있다. 
 비트리 간선(non-tree edge)이란 트리 간선이 아닌 나머지 모든 간선을
    (이미 어떤 방식으로든 방문/발견된 정점으로 가는 간선) 의미한다. 
# 예시
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'G': ['H'],
    'H': ['F'],
  }
def dfs(graph, start):
    visited = []
    back_edges = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            1) __________________________
        else:
            2) __________________________-
    return visited, sorted(list(back_edges))

내 답 
??? 여기서는 visited가 또 set이 아니네? > !!! 순서가 중요할 때는! List지!
1) visited.append(node) 
   stack.extend(graph[node])
2) #만약 visited에 있었다? 즉 방문한 곳이다. 근데 여기는 노드가 아니라 비트리 간선을 추가하는 것.. 
   그러니 출발점과 도착점이 있어야.. 중복인 경우는 처리가 안되는데. 상관이 .. 있는데. 쩝. 일단 내자.
    back_edges.add([node, graph[node]]) !!! 이거 안됨.. ! set은 원소를 hash처리하는데, list는 hashable하지 않음. 변할 확률이 높으니 python 자체에서 막아놓음. 그래서 튜플로 넣는게 좋았음. 튜플도 리스트가 원소로 있으면 안됨.
    ???왜 sorted로 back_edges를 조지지? 머 상관 없으려나.. 알파벳 순서의 문제니까.

맞아 !! 내가 헷갈렸던 것 : 이미 노드를 넣었기 때문에 누가 이 노드를 스택에 넣었는지를 알 수가 없었음.. 넣은 놈 - 노드 순으로 써야하는데. 

정답 : 

이건 함정 문제였음.
1) visit.append(node)
   for neighbor in graph.get(node, []) : #다음꺼를 neighbor라는 이름으로 불러옴.
    if neighbor not in visited : 다음꺼가 visited에 없는 경우, 즉 트리간선인경우
    stack.append(neighbor) #트리 간선 처리
    else : #비트리 간선인 경우
        back_edges.add((node, neigbor))

2) pass



뭔말인지는 알겠다. 핵심은 다음걸 먼저처리. 왜 ? 다음으로 넘어가면 이전단계가 누구였는지 알 수가 없음.
"""
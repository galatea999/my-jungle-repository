# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

"""

보자마자 딱 드는 생각.
Brute Force로 풀 수 있겠다. 
그래도 되나?
 2 <= N, M <= 10^2. O(n^2)가능. 무조건 된다.
 시간복잡도 됨. 

 idea
 1) 입력을 받은대로 칸을 만듦

 2)이동 함수를 만듦
count를 안에다 넣고 가야하나?
  종료조건 : 인덱스가 밖으로 나갈때
 [x][y] == 0 일때 
마지막 칸, 즉 [n][m]일때 : return 하면.. 끝나지 않나? 종료조건만 좀 고민해보자.

 이 칸이 1일때는  
 count+=1 하고 이어감
 상하좌우로.

"""

from collections import deque
n, m = map(int, input().split()) #이런 식으로 저장이 되시나?

board = [list(input()) for _ in range(n)] #걍 리스트 처리하면 쪼개진다고? 

def maze_escape(board):
    visited = [[0] * m for _ in range(n)]
    queue = deque()

    queue.append((0, 0))
    visited[0][0] = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    #BFS로 바뀜. 왤까. 왤까. 왤까. 생각해보자. 생각해보자.
    while queue:
        x, y = queue.popleft()

        #종료조건.
        if (x, y) == (n - 1, m - 1):
            return visited[x][y]

        #이건 뭐하는거지?: 상하좌우 가는걸 좌표 for문으로 특이하게 해결했네. 왜? 재귀가 아니니까? 
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            #내가 썼던 종료조건들 그대로. 이러면 1일때만 찾아가게 됨. 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == '0':
                continue
            if visited[nx][ny]:
                continue
            
            #반복 : 아. count를 visted에 넣어서 처리함. 아이디어 좋은데 이새끼? 
            #내가 문제를 잘못 생각했네. 관건은 1이 하나가 아닐때지. 그래서 DFS가 아닌거구나.
            # 
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

print(maze_escape(board))
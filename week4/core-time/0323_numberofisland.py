"""
Number Of Island
https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150

idea 
눈으로 보면 딱 보이는데.음..
추상적인 언어로 바꿔보자

output : 1 덩어리의 개수
한 덩어리의 조건 : 뭐 탐색을 통해 해결할 수 있나? 
1을 기준으로 오른쪽, 아래쪽으로 탐색을 간다고 생각해야할듯
그리고 결국은 전체를 탐색해야함. 
1이 나왔을 때 => 동료 찾기 모드. 오른쪽과 하단도 1인지 탐색=>
0이 나올때까지 반복. 0이 나오거나 그냥 끝나면 그때 섬 카운트 +1 
근데 이걸 백트래킹 형식으로 다시 돌아와야할 것 같은데? 
종료조건은 그러면 무엇이 되어야하지?

하나는 그렇게 찾을 수 있다고 치자. 
나머지 섬들은? 결국 모두를 다 탐색해야하니,
탐색한 곳은 다시 탐색하지 않는게 좋은데. 
탐색 check 판을 하나 더 만들어야할까.

함수 :
오른 쪽 한 칸 진행 -> 판별. 
아래쪽 한 칸 진행 -> 판별
1이다? checked 카운트 올리고 오른쪽 한 칸 진행. ->
0이다? 재귀의 맨 위로 돌아감. 그리고 1올림.

아래쪽 한 칸 진행 -> 판별,

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
       #grid와 같은 크기지만 값이 [0]인 checked를 만듦
        rows = len(grid)
        cols = len(grid[0])
        checked = [[0] * cols for _ in range(rows)] # 고치기

        #bt 함수를 정의함. 이거 처리를.. 어떻게 하지. 인덱스를 받아야하겠네.
        def bt(x, y) :
            if x<0 or x>= rows or y < 0 or y >= cols : #이 조건을 먼저 걸어줘야
                return
            if checked[x][y] :
                return #여기서 out of range가 안 남
            if grid[x][y] == '0' :  
                return
            
            checked[x][y] = 1


            bt(x+1,y)
            bt(x,y+1)
            bt(x-1, y)
            bt(x, y-1)
            #모두 다 돌고 맨 앞 원래 함수로 돌아왔으면 +1 추가

        for x in range(rows) : #가로 좌표
             for y in range(cols) : #세로 좌표
                if grid[x][y] == '1' and not checked[x][y] :
                    count += 1 
                    bt(x,y)
            

"""
여기서 못 짠건, 맨 앞 함수로 돌아왔을때만 1을 추가하는 방법과,
index가 out of range가 되려고 할 때의 처리
"""
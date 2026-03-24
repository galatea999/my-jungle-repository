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
        checked = [[0] * cols for _ in range(rows)] # 처음 부분은 가로를 만드는것, 뒤에 for 조건은 세로를 만드는 것
        count = 0 
        #bt 함수를 정의함. 이거 처리를.. 어떻게 하지. 인덱스를 받아야하겠네.
        def bt(x, y) :
            
            #Base case들을 미리 정의: x,y가 칸을 벗어날때, 이미 방문했을 때, 0인 부분일때
            if x<0 or x>= rows or y < 0 or y >= cols : 
                return
            if checked[x][y] :
                return 
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
        
        return count 

"""
결론적으로 완성함수는
checked를 통해 섬만 저장하는 함수로 바뀌었음. 
1을 만났을 때, 섬 갯수가 하나 올라가고 탐색함수가 섬 크기 탐색을 시작함. 
그리고 확인된 땅은 checked에 넣어 불필요한 계산을 막음. 
함수의 역할은 섬인지 아닌지 확인한다기보단 그냥 섬의 크기를 체크하는 것으로 바뀌었음. 뭘 위해? 중복에 빠져 영원히 재귀에서 도는걸 막기 위해.


"""
            

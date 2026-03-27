"""
클로드와 함께 공부하는 DP-practice 2


memo = {}
def top_down(m,n) :
    memo = {}
    if (m,n) in memo : 
        return memo[(m,n)] # ??? 이중배열이 낫나? 튜플로 키 형식이 낫나? in을 쓸거면 딕셔너리가 낫지 않나? 


    # (0,n), (m,0)일때까지 base case 쭉 만들기. 여기서 for문을 돌리면 안되지 않을까요. 재귀 돌릴거니까.
    시간 복잡도가 너무 커지거나 안 돌아가지 않을까.
    #그러면 bottom-up을 써보자. 변경! 이 포인트도 메모하자

"""

def dp_bottom_up(m,n) :
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1) :
        dp[i][0] = 1
    for j in range(n+1) :
        dp[0][j] = 1

    #for x, y in range(m, n) : 이건 안됨. 이중배열에선 튜플마냥 언패킹이 불가능
    for x in range(1, m+1) :
        for y in range(1,n+1):
            dp[x][y] = dp[x-1][y] + dp[x][y-1]
   
    return dp[m][n]

print(dp_bottom_up(2,3))
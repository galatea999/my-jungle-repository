"""

정수 n이 주어졌을 때, 1, 2, 3을 더해서 n을 만드는 경우의 수를 구하시오.
(순서가 다르면 다른 경우로 취급)
예) n=4 → (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2), (1+3), (3+1) → 7가지

이 함수는 무엇인가 => 점화식은 어떻게 쓰는가 => base case는 무엇인가 

근데 이러면 일단 memo하는 구조는 아닌데. 
"""


def dp(i) :
    if i == 1 :
        return 1
    if i == 2 :
        return 2
    if i == 3 :
        return 4
    
    return dp(i-1) + dp(i-2) + dp(i-3) # 생각의 근원 : Last Step 기법. 좀 더 스스로 설명해보기


memo = {} #??? memo를 dictionary 방식으로 저장. 하긴 굳이 list로 할 이유가 없나? 어떤 때에 list가 더 유리하지? 해시테이블이 검색 삽입 삭제 다 유리하잖아
#??? 함수 밖에서 써도 인덱스로 접근하고 추가가 가능한 이유는?
def dp_top_down(i) : # dp[n]부터 내려가며 필요한 것만 계산
    if i in memo : # ??? 이 in 함수를 list는 O(n)으로 처리하고 dict는 O(1)로 처리해서 dict를 쓰는거라고 봐야겠지?
        return memo[i] 
    
    if i == 1 :
        memo[i] = 1
        return 1
    if i == 2 :
        memo[i] = 2
        return 2
    if i == 3 :
        memo[i] = 4
        return 4
    
    memo[i] = dp_top_down(i-1) + dp_top_down(i-2) + dp_top_down(i-3)
    return memo[i]

def dp_bottom_up(i) : #dp[1]부터 올라가며 채움. bottom-up은 어차피 아래서부터 올라가서 조회를 할 일이 없으니 list를 써도 무방.... ???? 
    dp = [0] * (i+1) # ??? 왜 i+1? 1부터 시작하니까. 
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for n in range(4, i+1) :
        dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
    return dp[i]

print(dp_bottom_up(4) == 7)
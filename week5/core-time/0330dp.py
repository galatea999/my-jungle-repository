class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        문제 개 ㅈ밥같이 생겼는데.

        wordDict의 것들로 s를 만들 수 있느냐.
        함수. 조건. 
        in 체크, 그게 다가 아님
        DP면 메모하면서. 점화식. 베이스 케이스. 
        1 쪼개고 나머지를 반환하는 함수 ? 
        2 쪼개지느냐 아니냐?
        f(쪼개야 하는 함수) = 남은부분. 
        안쪼개지면 False
        f(s) = f
        이게 위에서 아래로 쪼개지는 느낌이라, 
        점화식으로 작은 구조로 쪼갠다는게 안 보임
        아래서 위로 가보자.
        """
            # word랑 나머지 부분으로 나누고 다시 탐색. 이걸 function으로 잡으면 되겠다.
        def func(word) : 
            #Base Case
            if word == [] :
                return True
            for ch in wordDict :
                if ch in s:
                    piece = #검증한 부분 빼고 나머지 부분 슬라이싱
                    #이 부분을 for문 돌릴게 아니라 함수로 써야겠네. 다시 들어가는 구조여야 하니.
        
                
                """
                #조건 잘못됨. 이러면 검증 다 못 하고 끝나버림. 이 조건을 DP로 빼야하나? 
                if not ch in s:
                    return False
                piece = # 검증한 부분 빼고 나머지 부분. 슬라이싱? 
                return func(piece) #결과 빼는 부분 더 고민. 여기를 dp처럼 메모형태로 빼야하나 ? 
        
        func(s)
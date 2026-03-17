"""
Constraint 
10^0 <= s, t <= 5 * 10^4

그러면 또 두번 돌면안돼. Brute Force 불가능...

Idea
애너그램의 조건  
1) 글자수가 같아야 함
2) 나오는 알파벳이 같아야 함
3) 나오는 알파벳의 수가 같아야함.

키와 밸류

1) s에 나온 글자를 키와 밸류로 저장. => 알파벳 각자에 카운팅을 올리는 식으로
2) 
3) 

최선의 경우 & 최악의 경우

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : #early return 역할 
            return False
        return sorted(s) == sorted(t)
        
        

# 다른 풀이

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26

        for ch in s :
            counts[ord(ch) - ord('a')] += 1

        for ch in t :
            counts[ord(ch) - ord('a')] -= 1

        return not any(counts)

"""
Time Complexity : O(n)
Space Complexity : O(1)
 (만약 뭐 유니코드 문자를 전부 받아야 했다면 그건 알파벳처럼 26개로 고정이 어려우니, 그 수만큼 dict를 만들어야했을것. 그러면 O(n))
"""
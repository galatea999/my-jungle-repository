# 49. Group Anagrams
# link : https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs : 
            key = tuple(sorted(word)) #key값 정함
            if key not in result : 
                result[key] = []
            result[key].append(word)
        
        return list(result.values())
            
    

    """
    결과와 인덱스로 연결 
    100자에, 총 갯수는 10^4
    idea
    원소들 하나하나 애너그램이 몇개 있는지 비교
    애너그램끼리 묶어서 return
    길이는 필요 없고, 정렬을 하거나 새로운 집합을 만들거나. 
    각자 정렬 후 비교 O Nlog N 그냥 하면 될듯? 
    같은 것들은 무엇이 같나? 집합이 같지.
    단어가 나올때마다 새로 만드는건 안좋은거같은데.. 몇갠지 알고. 
    보조자로 dict

    아이디어랑 막힌 포인트라도 정리를 해놓자. 내가 할 수 있는 일을 하자..
    키를 sorted로 하고, 밸류를 쟤네들로 하면 되지 않을까? 반대여야하나?
    1) strs로 for문을 돎
    2) 각각의 원소들을 sort하여 키값으로 쓰고, 밸류에 같은 단어들을 넣음
    ? 리스트는 키값으로 쓸 수 없음 => 그러면 다른걸로 쓰면 되지 않을까? 근데 함수를 모름. 
    3) 그리고 출력
    """


    """
    아이디어 : 
    왜 해시테이블이었나? 해시테이블보다는 key와 value의 묶음인 Dictionary가 필요했음.


    병목 : 
    - Dict의 key는 immutable만 가능하기 때문에 
    list는 키 값이 될 수 없었음 => tuple로 변환

    - 같은 key에 여러개의 value를 넣고 싶다면 
    그냥 무작정 추가하면 안됨(result[key] = word하면 덮어씌워짐)
    그 key의 value로 빈 리스트를 넣고, 거기에 append

    - dict의 value들만 출력하고 싶을때는 dict.values(), key는 dict.keys()겠지?

    이런거 무작정 들이 박는다고 알 수 잇는 거였나? 아니지..
    """

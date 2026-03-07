"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

짝수인 경우와 홀수인 경우를 먼저 판별해서 (%2가 0인지 1인지), 가운데 글자를 뺄지 말지를 정하고 가야할듯
짝수인 경우 : 그대로
홀수인 경우 : 가운데 문자 빼기 
9라고 치면, 9/2 = 4 나머지 1. 가운데는? 4+1
13이라고 치면, 13/2 = 6 나머지 1. 가운데는? 6+1. 이걸 활용해야겠네 

1, n / 2,n-1 / 3, n-2 ... / => j, n-j+1 둘이 같은지 비교

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama" 문장부호는 빼야하는구나! 그래!
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요 : 문자열을 뒤집는 아이디어 좋은데?
"""

def is_palindrome(s):
    """
    문자열이 회문인지 판별하는 함수
    
    Args:
        s: 판별할 문자열
    
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 힌트: isalnum() 메서드와 lower() 메서드 사용
    empty_list = []
    for ch in s :
        if ch.isalnum() :
            empty_list.append(ch)
    
    s = "".join(empty_list) #result += ch로도 처리가 가능하긴 함. 그러나 str이 immutable이라 매번 다시 정의하기때문에 비효율적)
    s=s.lower()


    # TODO: 정제된 문자열이 회문인지 확인하세요
    # 방법1: 문자열을 뒤집어서 비교 ([::-1] 사용)
    # 방법2: 양 끝 인덱스를 이용한 투포인터 방식? 
    
    #방법 1
    reverse_s = s[::-1]
    for i in range(len(s)) :
        if s[i] != reverse_s[i] :
            return False

        

    return True
    #return False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")



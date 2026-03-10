# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

#재귀 횟수에 따른 챗봇의 응답을 출력한다.
"""
재귀의 3조건
1. 자기자신을 포함하는 구조 
2. 그 근데 구조가 작아져야함
3. 베이스케이스

아니 한 줄 한 줄 넣어 놓으면 되나? 더 간단한 구조로 생각해보자. 
"""

how_many_recursion = int(input())



def again_again_again(num) :
    
    #Base case
    if num == 1 :
        print( """ 
"재귀함수가 뭔가요?"
"재귀함수는 자기 자신을 호출하는 함수라네"
 """)

    #마트료시카 부분
    else : 
        print( "____")  
        again_again_again (num-1)
        print("라고 답변하였지.")
again_again_again(how_many_recursion)
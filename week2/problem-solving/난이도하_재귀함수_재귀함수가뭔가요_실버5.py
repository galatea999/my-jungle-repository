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

num = int(input())



def sentence_recursion(num) :
    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

    def dfs(depth) :
        prefix = "____" * depth
        print("재귀함수가 뭔가요?")

        if depth == num :
            print( """ "재귀함수는 자기 자신을 호출하는 함수라네" """)
            return
        
        print(f"""{prefix * (depth+1)}잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
""")
        dfs(depth+1)
        print("라고 답변하였지.")

    dfs(0)

sentence_recursion(num)
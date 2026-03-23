# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

"""

idea
최단거리 찾기.
길게 풀어진 문장을 수학적이고 단조로운 언어로 바꿔보자.

n개의 노드가 주어졌을 때, 가장 적은 수로 n개를 모두 순회할 수 있는 방법을 찾아라.
 
단, 항상 이 노드들이 연결 그래프를 이룸.

간단하게 생각해보자. 간단하게.

다 연결되어있다면, 어떻게 해도 n-1 아닌가? 

뭐야이거
"""

number_test_case = int(input())

for _ in range(number_test_case) :
    
    inputs = list(map(int, input().split()))
    vertices = inputs[0]
    lines = inputs[1]
    for _ in range(lines) :
        k = input()
    
    print(inputs[0]-1)
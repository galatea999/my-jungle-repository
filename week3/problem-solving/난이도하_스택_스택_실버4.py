# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

how_many = int(input())

stack = []
result = []
for i in range(how_many) :
    cmd = input().split()
    if cmd[0] == "push" : #PUSH
        stack.append(int(cmd[1]))
    else : # 그 외 나머지
        if cmd[0] == "pop" :
            if stack :
                result.append(stack.pop())
            else :
                result.append(-1)

        elif cmd[0] == "size" :
            result.append(len(stack))
        
        elif cmd[0] == "empty" :
            if stack :
                result.append(0)
            
            else : 
                result.append(1)

        elif cmd[0] == "top" :
            if stack :
                result.append(stack[-1])
            
            else : 
                result.append(-1)

print("\n".join(map(str, result)))


"""
정답! 
이전에는 print가 많아 I/O(Input/Output출력에 쓰이는 비용이 컸음.
.append나 .pop은 메모리 안에서 처리하는 작업인 반면
input과 print는 밖이랑 주고 받는 작업이기 때문에 보통 더 느림
"""
"""
여기다 스택을 어떻게 적용한다? 
Last In First Out
요소를 스택에 위에서부터 하나씩 담아놓고, 처리한다?
처리 조건은?
스택으로 받을때는 뭐로 끊지? /=> 이거기준?
그러면 //이 여러개인건 ? => 일단 / 기준으로 끊어서 받으면 될 것 같은데. 
공백도 받아지나. 공백은 받을때 없애는걸로 하면 //, /// 해결
"""
#https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

#주소를 먼저 받기
# raw = input().split("/")
# stack = []
# result =[]
# for ch in raw :
#     if ch == '' :
#         continue
#     else : 
#         stack.append(ch)


# #하나씩 꺼내면서 결과에 추가
# while stack :
#     element = stack.pop()
#     #single quote=> 아무것도 하지 않기
#     if element == "." :
#         continue
#     # double quote => 이전으로 돌아가기. 
#     elif element == ".." :
#         if len(stack) == 0 : #### Python은 모든걸 객체로 저장하기 때문에, stack의 길이도 저장되어 있기에 O(1)임. 그리고 len 쓸 필요 없음
#             continue
#         else :
#             stack.pop()
        
#      # ...이나 ....은 그냥 파일 이름으로 취급
#     else :
#         result.append(element)


# print("/"+"/".join(result[::-1]))
        
#시간복잡도 : O(n)
#마지막으로 특이 케이스에 대해 생각. 
# 최소케이스 : /일때. 해결.
#  연속명령 : ///////


"""
for index, file in enumerate(files, 1) #enumerate 열거하다
튜플형태로 나옴. 좀 더 공부

처음부터 필요한것만 stack 했으면 시간복잡도를 2n에서 n으로 줄일 수 있었음.
"""

# 다시 쓴 코드

adress = input().split("/")

stack = []
for ch in adress :
    # if ch in ('', ".") :
    #     continue
    # elif ch == "." :
    #     continue
    if ch in ('', ".") : #더 clean한 코드. 
        continue 
    # elif ch == ".." :
    #     if not stack :
    #         continue
    #     else :
    #         stack.pop()
    if ch == ".." : #elif -> if로 바꾼 이유 : 의미상 그게 더 맞아서.
        if stack : #건너뛸건 먼저 버리고, 남은것만 다시 본다는 느낌으로 if
            stack.pop()
    else :
        stack.append(ch)

print("/"+"/".join(stack))

"""
이러면 시간복잡도가 n으로 절반이나 줄어 듦!
왜 이렇게 못 썼지? stack에 처음부터 억지로 써야한다고 생각해서.
그냥 필요한 것만 stack으로 담아도 됨.
근데 여기서 왜 stack이어야 했지 그러면? 
=> ..때문에. 아니었으면 다른 자료형도 크게 상관 없었음.
"""
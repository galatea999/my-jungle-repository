"""

Stack을 직접

구현해봅시다.

"""

class Stack :
    
    def __init__(self):
        self.stack=[]

    def add(self, element) :
        self.stack.append(element)

    def pop(self) :
        return self.stack.pop()
    
    
# s= Stack()
# s.add(10)
# s.add(20)
# s.add(30)

# while s.stack : # _.stack을 통해 클래스 안에 있는 리스트에 직접 접근
#     print(s.pop())


# 문자열을 받고, 문자열 내에 괄호가 있는지 검증하는 함수 


def lint(text) :
    check_brace = Stack()
    matching_brace = {"(":")", "{":"}","[":"]"}
    #Opening brace check
    for ch in text : 
        if ch in ["(","[","{"] :
            check_brace.add(ch)
    #Closing brace check
        elif ch in [")","]","}"] :
            
            if len(check_brace.stack) == 0 : #Java와 달리 Python에서는 Empty list에서 pop을 하면 오류가 떠버림
                return False 
            
            opening_brace = check_brace.pop()

            if ch != matching_brace[opening_brace] :
                return False
            
    if len(check_brace.stack) == 0  :
        return True
    
    else : 
        return False


        
            




print(lint("(나는 지금 여기에 살아있어"))
print(lint("(나는 지금 여기에 살아있어)"))
print(lint("(작은 숨을 내쉬며 살아있어}"))
# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
"""
Constraint
600,000 => 6* 10^5

명령어 개수 M 5 * 10^5

idea
고집 부리지 말고,문장으로 링크드 리스트를 구현하고,
커서를 헤드 역할을 하게 하자

1) 받은 문장으로 링크드리스트를 구현하기 => 각 단어들을 노드로 만들어야함 O(n)
2) 커서는 뭐.. 어렵지 않을 것 같은데

"""

class Node :
    def __init__(self, data) :
        self.data = data
        self.prev = None
        self.next = None

class LinkedList : 
    def __init__(self) :
        self.head = Node(None)
        self.tail = self.head
        self.cursor = self.head
        
        #새로운 노드를 맨 뒤에 추가
    def append(self, data) :
        new_node = Node(data)

        
        #두번째부터는 원래 테일이던 노드의 next를 새로 만든 테일로 수정해줌
        new_node.prev = self.tail
        self.tail.next = new_node
        #Tail을 New_node로
        self.tail = new_node

    def L(self) :

        if self.cursor == self.head :
            return #커서가 문장의 맨 앞일 때는 무시
        
        self.cursor = self.cursor.prev 

    def D(self) :

        if self.cursor == self.tail :
            return
        
        self.cursor = self.cursor.next

    def B(self) :
        #더미데이터를 가리키고 있는 경우 => 무시
        if self.cursor == self.head :
            return
        
        #마지막을 지울 경우
        if self.cursor == self.tail :
            self.cursor.prev.next = None
            self.cursor = self.cursor.prev
            self.tail = self.cursor
            return

        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev
        self.cursor = self.cursor.prev

    def P(self, char):
        new = Node(char)
        right = self.cursor.next   # 원래 커서 오른쪽 노드 저장

        new.prev = self.cursor
        new.next = right
        self.cursor.next = new

        if right:
            right.prev = new
        else:
            self.tail = new

        self.cursor = new
    # def P(self, char) :
    #     new = Node(char)
        
    #     new.next = self.cursor.next
    #     new.prev = self.cursor
    #     self.cursor.next.prev = new
    #     self.cursor.next = new
    #     self.cursor = self.next

    def print_list(self) :
        values = []

        current = self.head.next

        while current :
            values.append(current.data)
            current = current.next
        return values       

    
        
        

        #커서를 안으로 넣어서 만들까, 밖으로 뺄까. 일단 안에 넣어서 만들어보자
        #prev는 뒤로가기 위한 매개. 


        
sentence = input()
ll = LinkedList()

#링크드 리스트를 만든 상태
for ch in sentence :
    ll.append(ch)

ll.cursor = ll.tail

command_number = int(input())
while command_number :
     #여러개를 받는 P와 나머지를 일단 구분
    command = input().split()
    if command[0] == 'P' :
        ll.P(command[1])
    elif command[0] == 'L' :
        ll.L()
    elif command[0] == 'D' :
        ll.D()
    elif command[0] == 'B' :
        ll.B()
    command_number -= 1

print(''.join(ll.print_list()))


"""

핵심아이디어 : 
병목 :

"""

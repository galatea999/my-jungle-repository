"""

input = linked_list 2개 
역순으로 빼서 더하고 인풋하면 되잖아? 

링크드 리스트여야 한다는 점에서 아이디어를 못 잡겠다 .

링크드리스트는 
Constraint : 1<= 노드 갯수 <= 100

idea :

"""


l1 = input()
l2 = input()

l1 = int(''.join(l1[::-1]))
l2 = int(''.join(l2[::-1]))

result = l1 + l2
output = []
for num in result :
    output.append(num)

print(output[::-1])
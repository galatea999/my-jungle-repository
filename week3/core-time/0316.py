"""
Constraint
n logn으로 정렬하면 좋다.
logN으로 정렬하려면 퀵밖에 생각나는게 없는디
5 * 10^4 그러면 n^2은 안됨. Brute Force 탈락
음수도 나옴

idea :
Linked list는 삽입 삭제, 검색에 강점이 있고, Read는 걍 그럼 (하나씩 다 건너야하니)
data와 next가 있는 구조
그러면 Next들만 점검하면 되는거 아닌가. 
1) 탐색을 싹 하며, 빈 리스트에 추가. 가장 작은 값을 찾아 헤드로 놓음.
추가하는 과정에서 정렬하면 안되나? 검색과 삽입은 어차피 얼마 안 걸리잖아
리스트에는 4,2,1,3이 있을것. 이중에 1이 헤드.
2) 헤드를 찾고 나서 뭘 하지.. headㅇ


Test 
최소 : 마지막 케이스 점검.. 빈칸일때
연속입력 :

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
"""
linked_list = input()
head = 0
pointer = 1
#그냥 처음꺼 헤드로 잡고 숫자 두개 순차로 비교하면서 포인터만 계속 수정하면 되는거아니야?

for num in linked_list : 
    #최초 입력
    if not head : 
        head = num

    #헤드가 바뀌는 경우
    if num < head : 
        head = num
        head.next = num

    #헤드가 바뀌지 않는 경우. 비교하면서 들어가서 맞는 값이 나왔을 때.. next를 두개 바꿔주면 되지 안하. 



    
"""
Link : https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

 Average of Levels in Binary Tree


"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:


        q = deque([root])
        result = []
        while q :
            sum = 0.0
            length = len(q)
            for i in range(length) : #이 length가 level을 구분짓는 포인트였음. 전단계에서 추가한 만큼만 for문을 돌고, 새롭게 추가하고, 그 값들을 더해주는.
                current = q.popleft()
                
                if current.left :
                    q.append(current.left)

                if current.right :
                    q.append(current.right)

                sum += current.val
            
            result.append(sum / length)

        return result

        """
        내가 뭘 놓쳤을까? 
        """

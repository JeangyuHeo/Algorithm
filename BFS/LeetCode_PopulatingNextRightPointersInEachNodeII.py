"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        answer = []
        node_q = []
        
        node_q.append(root)
        
        while node_q:
            next_pointer = None
            for _ in range(len(node_q)):
                cur = node_q.pop(0)
                
                if cur.left:
                    node_q.append(cur.left)
                
                if cur.right:
                    node_q.append(cur.right)
                
                if next_pointer:
                    next_pointer.next = cur
                next_pointer = cur
                    
        return root
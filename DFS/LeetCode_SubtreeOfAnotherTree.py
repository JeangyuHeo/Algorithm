# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_subtree(tree, sub):
            if all([not tree, not sub]):
                return True
            if any([not tree and sub, tree and not sub]):
                return False
            if tree.val != sub.val:
                return False
            
            return check_subtree(tree.left, sub.left) and check_subtree(tree.right, sub.right)
        
        def dfs(tree):
            if tree:
                return check_subtree(tree, subRoot) or dfs(tree.left) or dfs(tree.right)
            return False
        
        return dfs(root)
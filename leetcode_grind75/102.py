#102. Binary Tree Level Order Traversal

#this is literally just bfs how did i forget this bruh I'm locked out
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lst = []
        q = deque()
        q.append(root)


        while q:
            level = []
            for _ in range(len(q)): # loops for every level
                node = q.popleft() #fifo
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                lst.append(level) #if level non-empty append the level to the list
        return lst
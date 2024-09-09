# 543. Diameter of Binary Tree

#nc solution will redo later
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(cur):
            if not cur:
                return 0
            
            left, right = dfs(cur.left), dfs(cur.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
        
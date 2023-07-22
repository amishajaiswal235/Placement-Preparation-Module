# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        if (root==None):
            return []
        else:
            ans.append(root.val)
            ans+=self.preorderTraversal(root.left)
            ans+=self.preorderTraversal(root.right)
            return ans
        
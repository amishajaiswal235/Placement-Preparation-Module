# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        if(root==None):
            return []
        else:
            ans+=self.postorderTraversal(root.left)
            ans+=self.postorderTraversal(root.right)
            ans.append(root.val)
            return ans
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        diff = [0]

        def height(root):
            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)
            difference = (left_height - right_height) if left_height > right_height else right_height - left_height
            diff[0] = max(diff[0],difference)
            

            return 1 + max(left_height, right_height)
        height(root)
        return diff[0] <= 1

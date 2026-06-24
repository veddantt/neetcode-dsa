# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        # Use a list to store the global maximum so it can be mutated inside the helper function
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # Recursively find the max path sum of the left and right subtrees
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # If a subtree path sum is negative, ignore it (clamp to 0)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Compute the max path sum passing *through* the current node as the highest point
            res[0] = max(res[0], node.val + left_max + right_max)

            # Return the maximum single branch sum extending upwards to the parent node
            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]
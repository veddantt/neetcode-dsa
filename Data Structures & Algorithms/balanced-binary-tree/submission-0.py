class Solution:
    def isBalanced(self, root):
        # Helper function returns a pair: [isBalanced (bool), height (int)]
        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # A node is balanced if left is balanced, right is balanced, 
            # AND their absolute height difference is no more than 1
            balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
            
            # Height of the current node is 1 + the max height of its children
            current_height = 1 + max(left[1], right[1])
            
            return [balanced, current_height]
            
        return dfs(root)[0]
class Solution(object):
    def goodNodes(self, root):
    
        if not root:
            return 0
        
        count = 0
        q = deque([(root, root.val)])
        
        while q:
            temp, maxi = q.popleft()
            
            if temp.val >= maxi:
                count += 1
            
            if temp.left:
                if maxi <= temp.left.val:
                    q.append((temp.left, temp.left.val))
                else:
                    q.append((temp.left, maxi))
            
            if temp.right:
                if maxi <= temp.right.val:
                    q.append((temp.right, temp.right.val))
                else:
                    q.append((temp.right, maxi))
        
        return count
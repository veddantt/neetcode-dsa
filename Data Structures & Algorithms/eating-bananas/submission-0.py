class Solution:
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        res = high
        
        while low <= high:
            # FORCE integer division using // instead of /
            mid = (low + high) // 2
            
            total_hours = 0
            for pile in piles:
                # Use pure integer arithmetic to simulate math.ceil()
                total_hours += (pile + mid - 1) // mid
                
            if total_hours <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return res
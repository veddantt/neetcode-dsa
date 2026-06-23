class Solution:
    def twoSum(self, numbers, target):
        # Initialize two pointers at the start and end of the array
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem requires 1-indexed positions
                return [left + 1, right + 1]
                
            elif current_sum < target:
                # Sum is too small, move left pointer right
                left += 1
            else:
                # Sum is too big, move right pointer left
                right -= 1
                
        return []
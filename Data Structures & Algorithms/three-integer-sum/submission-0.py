class Solution:
    def threeSum(self, nums):
        target = 0
        nums.sort()
        s = set()
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif current_sum < target:
                    j += 1
                else:
                    k -= 1
                    
        # Convert the set of unique triplets back into a list of lists
        output = [list(triplet) for triplet in s]
        return output
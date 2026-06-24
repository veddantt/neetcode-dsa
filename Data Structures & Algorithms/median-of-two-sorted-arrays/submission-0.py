class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to optimize binary search runtime to O(log(min(m, n)))
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
            
        n1, n2 = len(nums1), len(nums2)
        l, r = 0, n1
        total_half = (n1 + n2 + 1) // 2
        
        while l <= r:
            # FORCE integer division using //
            mid1 = (l + r) // 2
            mid2 = total_half - mid1
            
            # Determine boundary values around partitions
            maxLeft1 = nums1[mid1 - 1] if mid1 != 0 else float('-inf')
            minRight1 = nums1[mid1] if mid1 != n1 else float('inf')
            
            maxLeft2 = nums2[mid2 - 1] if mid2 != 0 else float('-inf')
            minRight2 = nums2[mid2] if mid2 != n2 else float('inf')
            
            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total elements combined is odd
                if (n1 + n2) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If total elements combined is even
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                
            elif maxLeft1 > minRight2:
                # Move left in nums1
                r = mid1 - 1
            else:
                # Move right in nums1
                l = mid1 + 1
                
        return 0.0
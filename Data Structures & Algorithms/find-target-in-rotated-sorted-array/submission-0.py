class Solution:
    def search(self, nums, target):
        s, e = 0, len(nums) - 1

        while s <= e:
            mid = s + (e - s) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[s] <= nums[mid]:
                if nums[s] <= target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1
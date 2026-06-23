from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []
            
        dq = deque()
        res = []

        for i in range(len(nums)):
            # 1. Remove elements from the back that are smaller than the current element
            # because they will never be the maximum in this or future windows
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 2. Add the current element's index to the back of the queue
            dq.append(i)

            # 3. Remove the index from the front if it has fallen out of the sliding window
            if dq[0] <= i - k:
                dq.popleft()

            # 4. Once our window reaches size k, start appending the maximums to our result
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
        
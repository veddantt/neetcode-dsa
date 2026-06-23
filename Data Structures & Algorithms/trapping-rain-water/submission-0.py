class Solution(object):
    def trap(self, height):
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        # Prefix calculation
        leftMax[0] = 0
        for i in range(1, n):
            leftMax[i] = max(height[i - 1], leftMax[i - 1])

        # Suffix calculation
        rightMax[n - 1] = 0
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(height[i + 1], rightMax[i + 1])

        ans = 0
        for i in range(n):
            waterLevel = min(leftMax[i], rightMax[i])
            if waterLevel >= height[i]:
                ans += waterLevel - height[i]
        return ans
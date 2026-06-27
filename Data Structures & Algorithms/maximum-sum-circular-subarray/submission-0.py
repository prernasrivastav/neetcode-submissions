class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        maxSum = nums[0]
        minSum = nums[0]
        curMax = 0
        curMin = 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)
            total += n
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -math.inf
        running_sum = 0
        for num in nums:
            running_sum += num
            maximum = max(running_sum, maximum)
            running_sum = max(0, running_sum)
        return maximum
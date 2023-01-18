class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        run_max = 0
        run_min = 0
        max_sum = nums[0]
        min_sum = nums[0]
        total = 0
        for num in nums:
            run_max = max(num, run_max + num)
            run_min = min(num, run_min + num)
            max_sum = max(max_sum, run_max)
            min_sum = min(min_sum, run_min)
            total += num

        return max_sum if 0 > max_sum else max(total - min_sum, max_sum)

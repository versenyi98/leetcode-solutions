class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[-1] + nums[i])
        return res
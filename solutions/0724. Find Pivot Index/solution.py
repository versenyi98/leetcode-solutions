class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        running = 0
        for idx, num in enumerate(nums):
            remaining = total - num
            if remaining == running:
                return idx
            total -= num
            running += num
        return -1

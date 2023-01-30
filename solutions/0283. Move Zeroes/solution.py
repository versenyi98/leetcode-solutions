class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        filtered = list(filter(lambda x: x, nums))
        for i in range(len(nums)):
            if i < len(filtered):
                nums[i] = filtered[i]
            else:
                nums[i] = 0
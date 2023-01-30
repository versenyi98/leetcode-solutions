class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        other = nums[-k:] + nums[:-k]
        for idx in range(len(nums)):
            nums[idx] = other[idx]
import bisect


def search_bin(lower, upper, nums, target):
    if lower > upper:
        return -1
    center = (lower + upper) // 2

    if nums[center] == target:
        return center
    if nums[center] > target:
        return search_bin(lower, center - 1, nums, target)
    return search_bin(center + 1, upper, nums, target)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search_bin(0, len(nums) - 1, nums, target)
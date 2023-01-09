def binary_search(lower, upper, arr, target):
    print(lower, upper, arr, target)
    if lower > upper:
        return lower

    center = (lower + upper) // 2

    num = arr[center]
    if num > target:
        if lower == upper:
            return lower
        return binary_search(lower, center -1, arr, target)
    elif num < target:
        if lower == upper:
            return lower + 1
        return binary_search(center + 1, upper, arr, target)
    return center


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary_search(0, len(nums) - 1, nums, target)
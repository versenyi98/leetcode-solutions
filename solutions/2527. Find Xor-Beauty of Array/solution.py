def xor(a, b, c):
    return ((a | b) & c)


class Solution:

    def xorBeauty(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maximum = max(nums)
        mask = 1

        arr = []

        while maximum >= mask:
            arr.append([])
            for num in nums:
                if mask & num:
                    arr[-1].append(num)
            mask *= 2

        res = 0
        for idx, elements in enumerate(arr):
            if len(elements) % 2 == 1:
                res += pow(2, idx)
        return res
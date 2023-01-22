class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1

        diffs = [num1 - num2 for num1, num2 in zip(nums1, nums2)]
        can_be_done = all(diff % k == 0 for diff in diffs) and sum(diffs) == 0

        if not can_be_done:
            return -1

        return sum(diff // k for diff in diffs)
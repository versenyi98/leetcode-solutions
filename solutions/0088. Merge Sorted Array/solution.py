class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        idx1, idx2 = 0, 0
        result = [0] * (n + m)
        while n + m:
            if not n:
                result[idx1 + idx2] = nums1[idx1]
                m -= 1
                idx1 += 1
            elif not m:
                result[idx1 + idx2] = nums2[idx2]
                n -= 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                result[idx1 + idx2] = nums1[idx1]
                m -= 1
                idx1 += 1
            else:
                result[idx1 + idx2] = nums2[idx2]
                n -= 1
                idx2 += 1
        for idx in range(len(nums1)):
            nums1[idx] = result[idx]

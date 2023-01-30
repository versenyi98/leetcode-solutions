class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set.intersection(set(nums1), set(nums2))
        return min(intersection) if len(intersection) else -1
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]
        
        result = []
        for first, second in zip(first_half, second_half):
            result.extend([first, second])

        return result
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = [0] * k

        running_sum = 0
        result = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k
            result += remainders[remainder]
            remainders[remainder] += 1

        return result + remainders[0]
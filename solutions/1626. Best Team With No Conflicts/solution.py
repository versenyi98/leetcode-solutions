class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        pairs = sorted(list(zip(scores, ages)))
        dp = [score for score, _ in pairs]
        print(dp)
        print(pairs)
        for i, (score, age) in enumerate(pairs):
            for j in range(0, i):
                other_score, other_age = pairs[j]
                if other_age <= age:
                    dp[i] = max(score + dp[j], dp[i])

        return max(dp)            
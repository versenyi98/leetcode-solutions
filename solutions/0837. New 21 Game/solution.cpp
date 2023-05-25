#include "../solution.hpp"

#include <vector>
#include <numeric>

double Solution::new21Game(int n, int k, int maxPts) {
    std::vector<double> dp(n + 1);

    dp[0] = 1.0;
    double s = k > 0 ? 1 : 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = s / maxPts;
        if (i < k) {
            s += dp[i];
        }
        if (i - maxPts >= 0 && i - maxPts < k) {
            s -= dp[i - maxPts];
        }
    }

    return std::accumulate(dp.begin() + k, dp.end(), 0.0);
}
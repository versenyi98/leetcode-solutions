#include <iostream>
#include <vector>

#include "../solution.hpp"

int main() {
    Solution solution;

    {
        std::vector<int> nums1 = {1, 3, 3, 2};
        std::vector<int> nums2 = {2, 1, 3, 4};
        int k = 3;

        std::cout << solution.maxScore(nums1, nums2, k) << std::endl;
    }

    {
        std::vector<int> nums1 = {4, 2, 3, 1, 1};
        std::vector<int> nums2 = {7, 5, 10, 9, 6};
        int k = 1;

        std::cout << solution.maxScore(nums1, nums2, k) << std::endl;
    }

    return 0;
}
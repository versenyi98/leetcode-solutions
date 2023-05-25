#include "../solution.hpp"

#include <algorithm>
#include <numeric>

long long Solution::maxScore(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
    std::vector<std::pair<long long, long long>> zipped = std::vector<std::pair<long long, long long>>(nums1.size());

    for (std::size_t i = 0; i < nums1.size(); i++) {
        zipped[i] = {nums2[i], nums1[i]};
    }

    std::sort(zipped.begin(), zipped.end(), std::greater<std::pair<long long, long long>>());

    std::vector<long long> heap;
    for (std::size_t i = 0; i < k; i++) {
        heap.push_back(zipped[i].second);
    }
    std::make_heap(heap.begin(), heap.end(), std::greater<long long>());

    long long sum = std::accumulate(heap.begin(), heap.end(), 0LL);
    long long current_maximum = zipped[k - 1].first * sum;

    for (std::size_t i = k; i < zipped.size(); i++) {
        std::pair<long long, long long> element = zipped[i];
        long long minimum = element.first;

        heap.push_back(element.second);
        std::push_heap(heap.begin(), heap.end(), std::greater<long long>());

        std::pop_heap(heap.begin(), heap.end(), std::greater<long long>());
        int back = heap.back();
        heap.pop_back();

        sum += element.second;
        sum -= back;

        current_maximum = std::max(current_maximum, sum * minimum);
    }

    return current_maximum;
}
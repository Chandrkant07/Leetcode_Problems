#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        long long cost = 0;
        
        // Monotonic decreasing deque storing pairs of {value, count_of_elements_covered}
        deque<pair<long long, int>> dq;
        
        int r = n - 1;
        for (int l = n - 1; l >= 0; --l) {
            long long val = nums[l];
            int count = 1;
            
            // Merge all elements to the right that are smaller than nums[l]
            while (!dq.empty() && dq.front().first < val) {
                auto [prev_val, prev_cnt] = dq.front();
                dq.pop_front();
                
                // These prev_cnt elements now need to be raised to 'val' instead of 'prev_val'
                cost += (val - prev_val) * prev_cnt;
                count += prev_cnt;
            }
            dq.push_front({val, count});
            
            // Shrink the window from the right if operations exceed k
            while (cost > k) {
                // The maximum element in [l, r] is always at the back of the deque
                long long max_val = dq.back().first;
                cost -= (max_val - nums[r]);
                
                dq.back().second--;
                if (dq.back().second == 0) {
                    dq.pop_back();
                }
                --r;
            }
            
            // All subarrays starting at l and ending in [l, r] are valid
            ans += (r - l + 1);
        }
        
        return ans;
    }
};

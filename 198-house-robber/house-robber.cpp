class Solution {
public:
    // void help(vector<int>& nums, vector<int> &dp){
    //     for(int i = 1; i<nums.size(); i++){
    //         int take = nums[i];
    //         if(i >1) take+=dp[i-2];
    //         int dontake = dp[i-1];
    //         dp[i] = max(take, dontake);
    //     }
    // }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n ==0) return 0;
        if (n == 1) return nums[0];

        int prev = nums[0], prev2 = -1, cur = nums[1];
        for(int i = 1; i<n; i++){
            int take = nums[i];
            if(i>1) take+= prev2;
            int notake = prev;
            cur = max(take,notake);
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }
};
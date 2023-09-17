class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for (int i = 0; i<nums.size(); i++){
            mp[nums[i]]++ ;
        }
        priority_queue<pair<int,int>, vector< pair<int,int> >, greater<pair<int,int> >> pq;
        for(auto it : mp){
            pq.push(make_pair(it.second, it.first));
            if (pq.size()>k) pq.pop();
        }
        vector<int> ans;
        while(!pq.empty()){
            pair<int, int> temp = pq.top();
            pq.pop();
            ans.push_back(temp.second);
        }
        return ans;
    }
};
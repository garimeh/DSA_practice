// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>
using namespace std;

struct interval{
    public :
    int start, end;
    // interval operator< 
    bool operator<(const interval& other) const {
        return start < other.start;
    }
};

bool compare(interval i1, interval i2){
    return (i1.start < i2.start);
}

vector<interval> merge(vector<interval> intvs){
    
    sort(intvs.begin(),intvs.end(),compare);
    int ind = 0;
    for(int i = 0; i < intvs.size(); i++){
        if(intvs[ind].end >= intvs[i].start){
            intvs[ind].end = max(intvs[ind].end,intvs[i].end);
        }
        else{
            ind++;
            intvs[ind] = intvs[i];
        }
    }
    return intvs;
}

int main() {
    vector<interval> intvs {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
    vector<interval> merged_intvs = merge(intvs);
    
    for (auto& intv : merged_intvs) {
        cout << "[" << intv.start << ", " << intv.end << "] ";
    }
    // Output: [1, 6] [8, 10] [15, 18]
    
    return 0;
    return 0;
}
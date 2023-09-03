class FrontMiddleBackQueue {
    vector<int> q;
    int count = 0;
    public:
    FrontMiddleBackQueue() {
        q.clear();
    }
    
    void pushFront(int val) {
        if (q.empty()) q.push_back(val);
        else q.insert(q.begin(), val);
        count++;
    }
    
    void pushMiddle(int val) {
        q.insert(q.begin()+count/2, val);
        count++;
    }
    
    void pushBack(int val) {
        q.push_back(val);
        count++;
    }
    
    int popFront() {
        if(q.empty()) return -1;
        int t = q[0];
        q.erase(q.begin());
        count--;
        return t;
    }
    
    int popMiddle() {
        if (q.empty()) return -1;
        int mid = 0;
        if(count % 2 == 0){
        mid = q[count/2-1];
        q.erase(q.begin()+count/2-1);
        }
        else{
            mid = q[count/2];
        q.erase(q.begin()+count/2);
        }
        count--;
        return mid;
    }
    
    int popBack() {
        if(q.empty()) return -1;
        int b = q[count-1];
        q.pop_back();
        count--;
        return b;
    }
};

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */
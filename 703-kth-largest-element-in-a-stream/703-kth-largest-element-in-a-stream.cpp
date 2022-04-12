class KthLargest {
public:
    priority_queue<int, std::vector<int>, std::greater<int>> pq{};
    int pq_size{};
    KthLargest(int k, vector<int>& nums) {
        pq_size = k;
        for(auto num : nums){
            pq.push(num);
            if(pq.size() > k){
                pq.pop();
            }
        }
    }
    
    int add(int val) {
        pq.push(val);
        if(pq.size() > pq_size){
            pq.pop();
        }
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
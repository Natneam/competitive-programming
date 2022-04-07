class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq{};
        int stoneOne{};
        int stoneTwo{};
        
        for(auto stone : stones) pq.push(stone);
        
        while(pq.size() > 1){
            stoneOne = pq.top();
            pq.pop();
            stoneTwo = pq.top();
            pq.pop();
            
            if(stoneOne != stoneTwo) pq.push(abs(stoneOne - stoneTwo));
        }
        
        return pq.size() == 0 ? 0 : pq.top();
        
    }
};
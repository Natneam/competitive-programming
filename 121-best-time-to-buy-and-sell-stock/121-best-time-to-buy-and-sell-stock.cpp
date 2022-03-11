#include <algorithm>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int ans = 0;
        int buy_price = prices[0];
        
        for(int i=1; i < prices.size(); i++){
            if (prices[i] <= buy_price){
                buy_price = prices[i];
            } else{
                ans = max(ans, prices[i] - buy_price);
            }
        }
        
        return ans;
        
    }
};
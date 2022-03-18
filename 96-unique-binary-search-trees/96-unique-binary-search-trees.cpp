class Solution {
public:
    int helper(int n, unordered_map<int, int>* memo){
        // memo = unordered_map<int, int>{};
        
        if(n <= 1) return 1;
        
        if (memo->find(n) != memo->end()) return (*memo)[n];
        
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            ans += helper(i, memo) * helper(n-i-1, memo);
        }
        
        (*memo)[n] = ans;
        return ans;
    }
    
    
    int numTrees(int n) {
        unordered_map<int, int> memo;
        return helper(n, &memo);
    }
};
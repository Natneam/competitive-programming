class Solution {
public:
    string getSmallestString(int n, int k) {
        vector<char> buffer;
        k -= n;
        
        for(auto i = 0; i < n; i++){
            if(k > 25){
                buffer.push_back(25 + 'a');
                k -= 25;
            } else{
                buffer.push_back(k + 'a');
                k = 0;
            }
        }
        string ans;
        for(int i = buffer.size() - 1; i >= 0; i--) ans.push_back(buffer[i]);
        
        return ans;
    }
};
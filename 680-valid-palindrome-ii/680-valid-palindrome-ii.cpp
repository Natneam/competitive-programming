class Solution {
public:
    bool helper(string s, int start, int end, bool pardoned){
        bool ans = false;
        while(start < end){
            if(s[start] == s[end]){
                start ++;
                end --;
            } else{
                if(pardoned) return false;
                pardoned = true;
                
                if (s[start] == s[end - 1]){
                    ans = helper(s, start + 1, end - 2, true);
                }
                
                if(!ans && s[start + 1] == s[end]){
                    ans = helper(s, start + 2, end - 1, true);
                } 
                
                return ans;
            }
        }
        
        return true;
    }
    
    bool validPalindrome(string s) {
        return helper(s, 0, s.size() - 1, false);
    }
};
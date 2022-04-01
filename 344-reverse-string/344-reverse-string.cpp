class Solution {
public:
    void reverseString(vector<char>& s) {
        int start{};
        int end{static_cast<int>(s.size()) - 1};
        char buffer{};
        
        while(start < end){
            buffer = s[start];
            s[start] = s[end];
            s[end] = buffer;
            
            start++;
            end--;
        }
    }
};
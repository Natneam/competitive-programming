class Solution {
public:
    int mySqrt(int x) {
        long start{0}, end{x}, mid{}, ans{};
        
        while(start <= end){
            mid = start + (end - start) / 2;
            if(mid * mid <= x){
                ans = mid;
                start = mid + 1;
            } else{
                end = mid -1;
            }
        }
        
        return ans;
    }
};
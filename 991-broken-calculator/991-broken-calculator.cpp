class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int count = 0;
        while(target > startValue){
           target = target % 2 == 0 ? target / 2 : target + 1;
            count += 1;
        }
        
        return count + startValue - target;
    }
};
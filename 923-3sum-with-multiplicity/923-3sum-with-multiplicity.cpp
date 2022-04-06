class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        //fix on of the numbers
        // do a two sum on the remainin ones
        
        long ans{};
        
        for(auto i=0; i < arr.size(); i ++){
            int elementsCount[101]{};
            int newTarget{target - arr[i]};
            
            for(auto j = i + 1; j  < arr.size(); j++){
                int a = newTarget - arr[j];
                if( 0 <= a and a < 101){
                    ans += elementsCount[a];
                }
                elementsCount[arr[j]] += 1;
            }
            
        }
        
        return ans % (static_cast<int>(pow(10, 9)) + 7);;
        
    }
};
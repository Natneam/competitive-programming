class Solution {
public:
    long check(vector<int> time, long long mid){
        long a = 0;
        
        for(auto t : time){
            a += mid / t;
        }
        
        return a;
    }
    
    long long minimumTime(vector<int>& time, int totalTrips) {
        
        long maximum = time[0];
        
        for(int i=1; i < time.size(); i++){
            if (time[i] > maximum){
                maximum = time[i];
            }
        }
        
        long start = 1;
        long end = totalTrips * maximum;
        long ans = totalTrips * maximum;
        
        while(start <= end){
            long mid = start + (end - start)/ 2;
            long value = check(time, mid);
            
            if (value < totalTrips){
                start = mid + 1;
            } else {
                end = mid - 1;
                if (mid < ans){
                    ans = mid;
                }
            }
        }
        
        return ans;
    }
};
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(target - x[0])/ x[1] for x in sorted(zip(position, speed), reverse=True)]
        ans = 0
        curr = 0
        
        for i in arr:
            if  i > curr:
                curr = i
                ans += 1
                
        return ans
        
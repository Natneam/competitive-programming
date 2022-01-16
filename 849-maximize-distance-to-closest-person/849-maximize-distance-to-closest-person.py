class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        persons = []
        for idx, seat in enumerate(seats):
            if seat == 1:
                persons.append(idx)
            
        ans = 0
        
        for i in range(1, len(persons)):
            diff =  persons[i] - persons[i-1]
            if diff//2 > ans:
                ans = diff//2 
        # try to put the person st the start of the array
        if persons[0] > ans:
            ans  = persons[0]
        
        # try to put the person st the last of the array
        if len(seats) - persons[-1] - 1 > ans:
            ans  = len(seats) - persons[-1] - 1
        
        return ans
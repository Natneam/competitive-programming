class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = counter = 0
        
        while True:
            i = i % len(tickets)
            tickets[i] -= 1
            
            if tickets[i] == 0 and i == k:
                return counter + 1
            
            if tickets[i] >= 0:
                counter += 1
            i += 1
        
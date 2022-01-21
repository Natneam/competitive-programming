class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cummulative = 0
        for i in range(len(gas)):
            cummulative += gas[i] - cost[i]
        
        if cummulative < 0:
            return -1
        
        gas_tank, recent_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            if gas_tank < 0:
                gas_tank = 0
                recent_index = i + 1
        
        return recent_index
    
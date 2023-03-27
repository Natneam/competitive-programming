class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        temp_queue = []
        visited = set(deadends)
        res = 0
        
        if "0000" in visited: return -1
        
        visited.add("0000")
        
        while queue or temp_queue:
            if not queue:
                queue = deque(temp_queue)
                temp_queue = []
                res += 1
                
            curr = queue.popleft()
            
            if curr == target:
                return res
            
            for i in range(4):
                num_1 = curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i+1:]
                num_2 = curr[:i] + str((int(curr[i]) - 1) % 10) + curr[i+1:]
                
                if num_1 not in visited:
                    temp_queue.append(num_1)
                    visited.add(num_1)
                    
                if num_2 not in visited:
                    temp_queue.append(num_2)
                    visited.add(num_2)
        
        return -1
        
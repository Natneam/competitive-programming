class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque([0])
        temp_queue = []
        visited = set([0])
        collection = defaultdict(set)
        
        for i in range(len(arr)):
            collection[arr[i]].add(i)        
        
        level = 0
        
        while queue or temp_queue:
            if not queue:
                queue = deque(temp_queue)
                # print(temp_queue)
                temp_queue = []
                level += 1
            index = queue.popleft()
            
            if index == len(arr) - 1:
                return level
            
            #go to index - 1
            if index - 1 not in visited and 0 <= index - 1 < len(arr):
                temp_queue.append(index - 1)
                visited.add(index - 1)
            #go to index + 1
            if index + 1 not in visited and 0 <= index + 1 < len(arr):
                temp_queue.append(index + 1)
                visited.add(index + 1)
            
            #go to neighbours
            for i in collection[arr[index]]:
                if i not in visited:
                    temp_queue.append(i)
                    visited.add(i)
            collection[arr[index]] = set()
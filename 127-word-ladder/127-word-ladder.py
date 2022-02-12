class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """        
        1. initialize the set for the words, visited set and a queue and secondary queue(temp_queue)
        2. add the beginword in the queue
        3. for each word in the queue, pop it form the queue and see for every variant of the word
        4. if the word is the end word and found in the set return the count 
        
        """
        def search_neighbour(node, wordSet):
            ans = []
            # print(node, wordSet)
            for i in range(len(node)):
                for j in range(26):
                    word = node[:i] + chr(ord('a') + j) + node[i+1:]
                    # print(word, end=" ")
                    if word in wordSet:
                        ans.append(word)
            # print()
            # print(ans)
            return ans
        
        
        queue = deque([])
        temp_queue = [beginWord]
        level = 0
        visited = set()
        wordSet = set(wordList)
        
        while queue or temp_queue:
            if not queue:
                queue = deque(temp_queue)
                temp_queue = []
                level += 1
            
            node = queue.popleft()
            
            if node == endWord:
                return level
            
            if node not in visited:
                visited.add(node)
                for n in search_neighbour(node, wordSet):
                    temp_queue.append(n)
            
        return 0

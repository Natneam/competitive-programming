class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        buckets = {}
        for word in words:
            if len(word) not in buckets:
                buckets[len(word)] = [word]
            else:
                buckets[len(word)].append(word)

        def do(buckets, prev, memo):
            if prev in memo:
                return memo[prev] - 1
            
            if len(prev) + 1 not in buckets:
                return 0
            
            res = 0
            for item in buckets[len(prev) + 1]:
                for i in range(len(item)):
                    if prev == item[:i] + item[i+1:]:
                        res = max(res, do(buckets, item, memo) + 1)
            memo[prev] = res
            return res
            
        res = 0
        memo = {}
        
        for item in sorted(words, key=lambda a : len(a)):
            res = max(res, do(buckets, item, memo) + 1)
        
        return res
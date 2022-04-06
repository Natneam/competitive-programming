class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        MOD = 1000000007
        
        for i in range(len(arr)):
            _map = defaultdict(int)
            new_target = target - arr[i]

            for j in range(i+1, len(arr)):
                if new_target - arr[j] in _map:
                    ans += _map[new_target - arr[j]]
                    ans %= MOD
                _map[arr[j]] += 1
            
        return ans
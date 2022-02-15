class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float("inf")
        
        for i in range(1, 7):
            counter = [[0, 0] for x in tops]
            for j in range(len(tops)):
                if tops[j] == i:
                    counter[j][0] = 1
                if bottoms[j] == i:
                    counter[j][1] = 1
            # print(counter)
            t = 0
            b = 0
            for c in counter:
                if c[0] != c[1]:
                    t += c[0]
                    b += c[1]
                elif c[0] == 0:
                    break
            else:
                ans = min(ans, min(t, b))
        return -1 if ans == float("inf") else ans
                        
                        
            
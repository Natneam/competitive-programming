class Solution:
    def numberOfWays(self, s: str) -> int:
        # idea => https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/1907109/python-dp-easy-to-understand
        comb = {"0" : 0, "10" : 0, "010" : 0, "1" : 0, "01" : 0, "101" : 0}

        for l in s:
            if l == "0":
                comb["0"] += 1
                comb["10"] += comb["1"]
                comb["010"] += comb["01"]
            else:
                comb["1"] += 1
                comb["01"] += comb["0"]
                comb["101"] += comb["10"]

        return comb["101"] + comb["010"]
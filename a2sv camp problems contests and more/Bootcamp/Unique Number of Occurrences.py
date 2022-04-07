# LINK TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-156/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequency = dict()
        for i in arr:
            if i in frequency.keys():
                frequency[i] += 1
            else:
                frequency[i] = 1
        return len(frequency.values()) == len(set(frequency.values()))
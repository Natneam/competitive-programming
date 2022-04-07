# LINK TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-88/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        output = ""
        
        totalShifts = sum(shifts)
        prevShifts = 0
        
        for i in range(len(S)):
            output += self.shift(S[i], totalShifts - prevShifts)
            prevShifts += shifts[i]
        return output
        
    def shift(self, letter, shift):
        return chr((ord(letter) - 97 + shift)%26 + 97 ) 
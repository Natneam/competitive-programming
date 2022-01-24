class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        arr = [0, 0] # small, upper
        for l in word:
            if l.isupper():
                arr[1] += 1
            else:
                arr[0] += 1
        
        length = len(word)
        
        return arr[0] == length or arr[1] == length or (arr[1] ==  1 and word[0].isupper())
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def check_letters(w, upper=True):
            for l in w:
                if upper:
                    if l.islower():
                        return False
                else:
                    if l.isupper():
                        return False
            return True
                    
                    
        
        return check_letters(word) or check_letters(word, upper=False) or (word[0].isupper() and check_letters(word[1:], upper=False))
        
        
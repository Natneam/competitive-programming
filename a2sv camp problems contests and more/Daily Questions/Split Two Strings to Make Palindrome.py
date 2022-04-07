class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if self.isPalindrom(a) and self.isPalindrom(b):
            return True
        
        startIndex = 0
        endIndex = len(a) - 1
        wayOne = True
        wayTwo = True
        
        while startIndex < endIndex:
            
            if wayOne and a[startIndex] != b[endIndex]:
                wayOne = False
                if self.isPalindrom(a[startIndex:endIndex+1]) or self.isPalindrom(b[startIndex:endIndex+1]):
                    return True
            if wayTwo and b[startIndex] != a[endIndex]:
                wayTwo = False
                if self.isPalindrom(a[startIndex:endIndex+1]) or self.isPalindrom(b[startIndex:endIndex+1]):
                    return True
                
            if not wayOne and not wayTwo:
                return  False
            
            startIndex += 1
            endIndex -= 1
            
        return True
        
        
        
        
    def isPalindrom(self, word):
        startIndex = 0
        endIndex = len(word) - 1
        while startIndex <= endIndex:
            if word[startIndex] != word[endIndex]:
                return False
            startIndex += 1
            endIndex -= 1
        return True

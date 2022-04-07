# LINK TO THE PROBLEM => https://leetcode.com/problems/replace-words/

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEnd = False
        
class Tries:
    def __init__(self):
        self.head = Node(None)
    
    
    def insert(self, word):
        curr = self.head
        for letter in word:
            if letter not in curr.children.keys():
                curr.children[letter] = Node(letter)
            curr = curr.children[letter]
        curr.isEnd = True
    
    def search(self, word):
        #customized search
        # return index if > 0: just use the original word else use the sliced word
        # becarefull of offbyone error
        count = 0
        curr = self.head
        for letter in word:
            if curr.isEnd:
                return count
            
            if letter not in curr.children.keys():
                return 0
            count += 1
            curr = curr.children[letter]
        return 0
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # polulate the root words in a tries
        tries = Tries()
        for word in dictionary:
            tries.insert(word)
        
        sentenceArr = sentence.split(" ")
        for i in range(len(sentenceArr)):
            rootLen = tries.search(sentenceArr[i])
            if rootLen > 0:
                sentenceArr[i] = sentenceArr[i][:rootLen]
        return " ".join(sentenceArr)
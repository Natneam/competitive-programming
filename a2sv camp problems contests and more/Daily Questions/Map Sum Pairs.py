# LINK TO THE PROBLEM => https://leetcode.com/problems/map-sum-pairs/

class Node:
    def __init__(self, descendantsSum, letter=None):
        self.letter = letter
        self.children = dict()
        self.descendantsSum = descendantsSum
                
class Trie:
    def __init__(self):
        self.head = Node(0)
        self.words = dict()
    
    def addWord(self, word, value):
        currNode = self.head
        newWord = False
        
        if word not in self.words:
            newWord = True
            self.words[word] = value
        
        for letter in word:
            if letter in currNode.children:
                newVal = value
                if not newWord:
                    newVal = value - self.words[word]
                currNode.children[letter].descendantsSum += newVal
            
            else:
                currNode.children[letter] = Node(value, letter)
            
            currNode = currNode.children[letter]
            
        self.words[word] = value
    
    
    def searchPref(self, prefix):
        currNode = self.head
        
        for letter in prefix:
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                return 0
            
        return currNode.descendantsSum
        
        
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.addWord(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.searchPref(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

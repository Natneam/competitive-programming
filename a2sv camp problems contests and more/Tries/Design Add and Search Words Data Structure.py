# LINK TO THE PROBLEM => https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)
        

    def addWord(self, word: str) -> None:
        curr = self.head
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node(letter)
            curr = curr.children[letter]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        return self.customSearch(word, self.head)
    
    
    def customSearch(self, word, curr):
        for index in range(len(word)):
            if word[index] == ".":
                val = False
                for i in curr.children.keys():
                    val = val or self.customSearch(word[index+1:], curr.children[i])
                return val
            if word[index] not in curr.children:
                return False
            curr = curr.children[word[index]]
        return curr.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
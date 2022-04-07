# LINK TO THE PROBLEM => https://leetcode.com/problems/implement-trie-prefix-tree/


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEnd = False
        
    

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.head
        for letter in word:
            if letter not in currNode.children.keys():
                currNode.children[letter] = Node(letter)
            currNode = currNode.children[letter]
        currNode.isEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.head
        for letter in word:
            if letter in currNode.children.keys():
                currNode = currNode.children[letter]
            else:
                return False
        return currNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.head
        for letter in prefix:
            if letter in currNode.children.keys():
                currNode = currNode.children[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
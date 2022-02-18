class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie: 
                trie[letter] = {}
            trie = trie[letter]
        
        trie['#'] = 0

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter in trie:
                trie = trie[letter]
            else:
                return False
            
        if '#' in trie:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter in trie:
                trie = trie[letter]
            else:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
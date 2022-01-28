class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node["#"] = '#'

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.trie)
    
    def search_helper(self, word, index, node):
        for i in range(index, len(word)):
            l = word[i]
            if l != '.':
                if l in node:
                    node = node[l]
                else:
                    return False
            else:
                for n in node:
                    if n != '#'and self.search_helper(word, i+1, node[n]):
                        return True
                return False
            
        return '#' in node


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
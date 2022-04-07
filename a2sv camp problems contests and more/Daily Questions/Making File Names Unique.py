# LINK TO THE PROBLEM => https://leetcode.com/problems/making-file-names-unique/

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        class Node:
            def __init__(self, letter=None):
                self.letter = letter
                self.nextK = 1
                self.children = {}
                self.isEnd = False
        
        class Tries:
            def __init__(self):
                self.head = Node()
            
            def add_word(self, word):
                currNode = self.head
                letters = word.split('(')
                word = []
                for i in range(len(letters)):
                    k = letters[i]
                    if ')' not in k:
                        for j in k:
                            word.append(j)
                    else:
                        word.append('(')
                        word.append(k[:-1])
                        word.append(k[-1:])
                
                for letter in word:
                    if letter not in currNode.children.keys():
                        currNode.children[letter] = Node(letter)
                    currNode = currNode.children[letter]
                    
                if currNode.isEnd:
                    # add self.nextK to the tries
                    if '(' not in currNode.children.keys():
                        currNode.children['('] = Node('(')
                    currNode = currNode.children['(']
                    while True:                        
                        if str(currNode.nextK) not in currNode.children.keys():
                            word = word + ['(' + str(currNode.nextK) + ')']
                            currNode.children[str(currNode.nextK)] = Node(str(currNode.nextK))

                            currNode = currNode.children[str(currNode.nextK)]
                            currNode.children[')'] = Node(')') 
                            currNode.children[')'].isEnd = True
                            break
                        if not currNode.children[str(currNode.nextK)].children[')'].isEnd:
                            currNode.children[str(currNode.nextK)].children[')'].isEnd = True
                            word = word + ['(' + str(currNode.nextK) + ')']
                            break
                        currNode.nextK += 1
                else:
                    currNode.isEnd = True
                return "".join(word)
                    
            
        tries = Tries()
        for index in range(len(names)):
            names[index] = tries.add_word(names[index])
        return names
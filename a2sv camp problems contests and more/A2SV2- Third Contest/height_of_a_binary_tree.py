# LINK TO THE PROBLEM => https://www.hackerrank.com/contests/a2sv-contest-3/challenges/tree-height-of-a-binary-tree/submissions/code/1329819830

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    return count_node(root) - 1

def count_node(root):
    if root == None:
        return 0
    h1 = 1 + count_node(root.left)
    h2 = 1 + count_node(root.right)
    return h1 if h1 >= h2 else h2
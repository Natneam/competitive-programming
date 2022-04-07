# LINK TO THE PROBLEM => https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        rule = {')':'(', ']':'[', '}':'{'}
        if len(s) == 0: return True
        elif len(s) == 1: return False
        
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                try:
                    if rule[i] != stack.pop():
                        return False
                except:
                    return False
        return True if len(stack) == 0 else False
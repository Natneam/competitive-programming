# LINK TO THE PROBLEM => https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        counter = 1
        targetIndex = 0
        while targetIndex < len(target):
            if counter == target[targetIndex]:
                operations.append('Push')
                targetIndex += 1
            else:
                operations.append('Push')                
                operations.append('Pop')
            counter += 1
        return operations
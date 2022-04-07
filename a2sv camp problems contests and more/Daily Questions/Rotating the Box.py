# LINK TO THE PROBLEM => https://leetcode.com/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        #rotating the box 90deg clockwise
        newBox = [[0 for _ in range(len(box))] for __ in range(len(box[0]))]
        for i in range(len(box)):
            for j in range(len(box[0])):
                newBox[j][len(box)-1-i] = box[i][j]
        
        #applying the gravity property
        for j in range(len(newBox[0])):
            spotsNum = 0
            stonesNum = 0
            for i in range(len(newBox)):
                if newBox[i][j] == "*":
                    self.applyGravity(newBox, spotsNum, stonesNum, i-1, j)
                    stonesNum = 0
                    spotsNum = 0
                else:
                    spotsNum += 1
                
                if newBox[i][j] == "#":
                    stonesNum += 1
                
            self.applyGravity(newBox, spotsNum, stonesNum, i, j)
        
        return newBox
    
    def applyGravity(self, box, spotsNum, stonesNum, i, j):
        for k in range(spotsNum):
            if stonesNum > 0:
                box[i-k][j] = '#'
                stonesNum -= 1
            else:
                box[i-k][j] = '.'


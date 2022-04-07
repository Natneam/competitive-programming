# LINK TO THE PROBLEM => https://leetcode.com/problems/reorganize-string/
class Solution:
    def reorganizeString(self, S: str) -> str:
        S = list(S)
        lenS = len(S)
        rearrangedS = []
        traversedItems = [] # list of Items which cannot be inserted in the 'being build' list at specific point in time
        for i in S:
            flag = False
            for j in range(len(rearrangedS)):
                if rearrangedS[j] != i:
                    if j == 0:
                        rearrangedS.insert(j,i)
                        flag = True
                        break
                    elif j == len(rearrangedS)-1:
                        rearrangedS.append(i)
                        flag = True
                    else:
                        if rearrangedS[j-1] != i:
                            rearrangedS.insert(j,i)
                            flag = True
                            break
                        
                    
            if flag == False and len(rearrangedS) != 0:
                traversedItems.append(i)
                S.append(i)
                if (len(rearrangedS) + len(traversedItems))%lenS == 1:
                    return ''
            if len(rearrangedS) == 0:
                rearrangedS.append(i)
        # print(rearrangedS)
        return ''.join([x for x in rearrangedS])
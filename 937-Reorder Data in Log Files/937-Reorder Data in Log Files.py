class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for l in logs:
            if l.split()[1].isdigit():
                digit.append(l)
            else:
                letter.append(l)
        
        for i in range(len(letter)):
            letter[i] = letter[i].split()
            letter[i] = [letter[i][1:], letter[i][0]]
        letter.sort()

        for i in range(len(letter)):
            letter[i] = letter[i][1] + " " + " ".join(letter[i][0])
        
        return letter + digit
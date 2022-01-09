class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        north = 0
        east = 0
        direction = 0 #0 : N, 1 : E, 2: S, 3 : W
        
        for i in instructions:
            if i == 'G':
                if direction == 0:
                    north += 1
                elif direction == 2:
                    north -= 1
                elif direction == 1:
                    east += 1
                else:
                    east -= 1
            elif i == "R":
                direction += 1
                direction %= 4
            else:
                direction -= 1
                if direction == -1:
                    direction = 3
        
        if (north, east) == (0, 0):
            return True
        
        return direction != 0
    
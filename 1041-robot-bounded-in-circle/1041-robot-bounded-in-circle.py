class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # either the robot should have different direction than the direction it started with
        # or the end should end on the start point
        x, y = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        
        for ins in instructions:
            if ins == 'G':
                x, y = x + directions[curr_dir][0], y + directions[curr_dir][1]
            else:
                curr_dir += 1 if ins == "R" else - 1
            curr_dir = curr_dir % 4

        return curr_dir != 0 or (x, y) == (0, 0)

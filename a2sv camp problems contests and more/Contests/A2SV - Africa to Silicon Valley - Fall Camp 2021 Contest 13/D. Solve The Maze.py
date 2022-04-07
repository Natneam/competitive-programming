import sys
sys.setrecursionlimit(10**6)

def block(grid, i, j):
    directions = [(0, 1), (0, -1), (1,0), (-1,0)]

    for direction in directions:
        new_x = direction[0] + i
        new_y = direction[1] + j
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if  grid[new_x][new_y] == '.':
                grid[new_x][new_y] = '#'
            elif grid[new_x][new_y] == 'G':
                return False
    return True
        
        
    
def dfs(grid, coordinate, visited):
    if not (0 <= coordinate[0] < len(grid) and 0 <= coordinate[1] < len(grid[0])) or grid[coordinate[0]][coordinate[1]] == "#":
        return 0
    
    directions = [(0, 1), (0, -1), (1,0), (-1,0)]

    visited.add(coordinate)

    val = 1 if grid[coordinate[0]][coordinate[1]] == "G" else 0
    for direction in directions:
        new_x = direction[0] + coordinate[0]
        new_y = direction[1] + coordinate[1]
        if (new_x, new_y) not in visited:
            val += dfs(grid, (new_x, new_y), visited)
    
    return val 

def solve(grid):
    good_guys = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "G":
                good_guys += 1
            elif grid[i][j] == "B":
                if not block(grid, i, j):
                    return False
    reachable = dfs(grid, (len(grid) - 1, len(grid[0]) - 1), set())
    return reachable == good_guys

def main():
    t = int(input())
    answers = []
    for _ in range(t):
        grid = []
        n, m = list(map(int, input().split()))
        for i in range(n):
            grid.append(list(input()))
        answers.append(solve(grid))
    a = ["NO", "YES"]
    for ans in answers:
        print(a[ans])


if __name__ == "__main__":
    main()

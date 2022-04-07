board_size = int(input())

queen = list(map(int, input().split()))
king_start = list(map(int, input().split()))
king_end = list(map(int, input().split()))

def which_quadrant(origin, point):
    x, y = point

    if x < origin[0]:
        #2 or 3
        if y < origin[1]:
            return 3
        else:
            return 2
    else:
        # 1 or 4
        if y < origin[1]:
            return 4
        else:
            return 1


if which_quadrant(queen, king_start) == which_quadrant(queen, king_end):
    print("YES")
else:
    print("NO")
        
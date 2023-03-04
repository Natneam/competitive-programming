for _ in range(int(input())):
    input()
    row1 = input()
    row2 = input()

    curr_row = 0
    curr_col = 0

    for i in range(len(row1)):
        if row1[i] == row2[i] == "1":
            print("NO")
            break
    else:
        print("YES")
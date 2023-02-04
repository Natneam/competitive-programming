test = int(input())

for _ in range(test):
    _ = input()
    ans = 0
    enemy = list(input())
    george = list(input())
    for i in range(len(enemy)):
        if george[i] == "1":
            if enemy[i] == "0": 
                enemy[i] = "2"
                ans += 1
            else:
                if (i > 0 and enemy[i - 1] == "1"):
                    enemy[i - 1] = "2"
                    ans += 1
                elif (i < len(enemy) - 1 and enemy[i + 1] == "1"): 
                    enemy[i + 1] = "2"
                    ans += 1
    print(ans, end = "\n")
                
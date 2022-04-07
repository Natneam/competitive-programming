def solve(posts, dorms):
    dorms = [0] + dorms
    for i in range(len(dorms)-1):
        dorms[i+1] = dorms[i+1] + dorms[i]

    answers = []
    index = 0
    for post in posts:
        while post > dorms[index]:
            index += 1
        answers.append([index, post -dorms[index-1]])
    return answers

def main():
    n, m = list(map(int, input().split()))
    dorms = list(map(int, input().split()))
    posts = list(map(int, input().split()))

    answers = solve(posts, dorms)

    for line in answers:
        print(*line, sep=" ", end="\n")

if __name__ == "__main__":
    main()
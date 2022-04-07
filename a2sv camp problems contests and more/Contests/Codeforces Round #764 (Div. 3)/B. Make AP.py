def main():
    for i in range(int(input())):
        a, b, c = list(map(int, input().split()))
        if (2*b - c) % a == 0 and(2*b - c) // a > 0 :
            print("YES", end="\n")
        elif (2*b - a) % c == 0 and (2*b - a) // c > 0  :
            print("YES", end="\n")
        elif (a + c) % (2 * b) == 0 and (a + c) // (2 * b) > 0:
            print("YES", end="\n")
        else:
            print("NO", end="\n") 


if __name__ == "__main__":
    main()
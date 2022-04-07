def is_palidrom_and_10(string):
    for i in range(len(string)//2 + 1):
        if string[i] != string[len(string) - 1 -i] or string[i] == "?" or string[len(string) - i - 1] == "?":
            return False
    return True

def solve(a, b, string):
    for i in range(len(string)):
        if string[i] == "1":
            if string[len(string) - 1 - i] == "?":
                string[len(string) - 1 - i] = "1"
        elif string[i] == "0":
            if string[len(string) - 1 - i] == "?":
                string[len(string) - 1 - i] = "0"

    for i in range(len(string)):
        if string[i] == "1":
            b -= 1
        elif string[i] == "0":
            a -= 1

    if a % 2 == 0:
        i = 0
        while i < len(string) and a > 0:
            if string[i] == "?":
                string[i] = '0'
                a -= 1
            if string[len(string) - i - 1] == "?":
                string[len(string) - i - 1] = '0'
                a -= 1
            
            i+=1
        
        i = 0
        
        while i < len(string) and b > 0:
            if string[i] == "?":
                string[i] = '1'
                b -= 1
            if string[len(string) - i - 1] == "?":
                string[len(string) - i - 1] = '1'
                b -= 1
            i+=1
        
    else:
        i = 0
        while i < len(string) and b > 0:
            if string[i] == "?":
                string[i] = '1'
                b -= 1
            if string[len(string) - i - 1] == "?":
                string[len(string) - i - 1] = '1'
                b -= 1
            i+=1
        i = 0
        while i < len(string) and a > 0:
            if string[i] == "?":
                string[i] = '0'
                a -= 1
            if string[len(string) - i - 1] == "?":
                string[len(string) - i - 1] = '0'
                a -= 1
            
            i+=1
    if not is_palidrom_and_10(string) or a != 0 or b != 0:
        return -1
    
    return "".join(string)

def main():
    t = int(input())
    for _ in range(t):
        a, b = list(map(int, input().split()))
        string = list(input())
        print(solve(a, b, string), end="\n")

if __name__ == "__main__":
    main()
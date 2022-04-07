from typing import Counter


def main():
    t = int(input())
    for _ in range(t):
        input()
        lst = map(int, input().split())
        counter = Counter(lst)
        count = 0
        
        for key in counter:
            if counter[key] > 1 and -key not in counter and key != 0:
                count += 1
        
        print(count + len(counter))

if __name__ == "__main__":
    main()

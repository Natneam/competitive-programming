from typing import DefaultDict


def main():
    for i in range(int(input())):
        n = int(input())
        nums = DefaultDict(set)
        lst = list(map(int, input().split()))

        for i, num in enumerate(lst):
            while num >= 1:
                if num <= n:
                    nums[i].add(num)

                num = num // 2
                  
        for i in range(n, 0, -1):
            for k in nums:
                if i in nums[k]:
                    del nums[k]
                    break
        
        print("YES" if len(nums) == 0 else "NO", end="\n")

            
            
            


if __name__ == "__main__":
    main()
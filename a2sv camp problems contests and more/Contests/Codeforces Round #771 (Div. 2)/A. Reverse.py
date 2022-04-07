for i in range(int(input())):
    input()
    nums =  list(map(int, input().split()))
    c_n = list(sorted(nums))
    nums = list(map(str, nums))
    broken = False
    for i in range(len(c_n)):
        if str(c_n[i]) != nums[i]:
            x = nums.index(str(c_n[i]))
            print(" ".join(nums[:i] + list(reversed(nums[i:x+1])) + nums[x+1:]), end="\n")
            broken = True
            break
    if not broken:
        print(" ".join(nums), end="\n")

    

test_cases = int(input())
answers = []

for i in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    sum_nums = sum(nums)
    sum_of_the_removed = sum_nums - (sum_nums*(n-2))/n


    map_of_nums = {}
    for num in nums:
        if num in map_of_nums:
            map_of_nums[num] += 1
        else:
            map_of_nums[num] = 1
    

    count = 0

    for i in range(len(nums)):
        map_of_nums[nums[i]] -= 1
        if map_of_nums[nums[i]] == 0:
            del map_of_nums[nums[i]]
        
        find = sum_of_the_removed - nums[i]
        if find in map_of_nums:
            count += map_of_nums[find]
    answers.append(count)

for answer in answers:
    print(answer)


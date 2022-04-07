dp = {}

def paint_house(costs, memo, house=0, exclude=None,):
    if (house, exclude) in memo:
        return memo[(house, exclude)]
    
    val = float('inf')

    if house >= len(costs):
        return 0
    
    #find the two minimums
    min1, min2 = 0, 0

    for i in range(len(costs[house])):
        if i != exclude and costs[house][i] <= costs[house][min1]:
            min2 = min1
            min1 = i

    val = float('inf')

    for i in [min1,min2]:
        val = min(val, paint_house(costs, memo, house + 1, i) + costs[house][i])
    memo[(house, exclude)] = val
    return memo[(house, exclude)]
print(paint_house(tuple((17,2,i) for i in range(100)), dp))
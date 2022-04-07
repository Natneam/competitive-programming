size = 10
parents = [x for x in range(size)]
size_arr = [1]*size

def find(a):
    parent = a

    while parent != parents[parent]:
        parent = parents[parent]
    
    curr_node = a
    while curr_node != parent:
        temp_node = curr_node
        curr_node = parents[curr_node]
        parents[temp_node] = parent
    return parent


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    parents[parent_b] = parent_a
    size_arr[parent_b] = size_arr[parent_a] + size_arr[parent_b]


print(parents, size_arr)

union(1, 0)
union(0, 2)
union(2, 3)
union(3, 4)
union(4, 5)
union(5, 6)
union(6,7)
union(8,9)

# for i in range(size):
#     find(i)

print(parents, size_arr)
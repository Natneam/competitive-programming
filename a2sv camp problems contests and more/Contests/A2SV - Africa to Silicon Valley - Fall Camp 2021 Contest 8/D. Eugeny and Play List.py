n, m = list(map(int, input().split()))
time_line = {}

prev_time = 0
for i in range(1, n+1):
    c, t = list(map(int, input().split()))
    time_line[(prev_time, prev_time + (c*t))] = i
    prev_time = prev_time + (c*t)

queries = sorted(list(map(int, input().split())))
index = 0

for time_stamp in sorted(time_line.keys()):
    while index < len(queries) and time_stamp[0] < queries[index] <= time_stamp[1]:
        print(time_line[time_stamp])
        index += 1
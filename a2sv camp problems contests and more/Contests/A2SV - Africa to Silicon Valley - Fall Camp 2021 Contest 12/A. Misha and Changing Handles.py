def solve(graph):
    visited = set()
    answers = {}

    for item in graph:
        if item not in visited:
            changed_to = graph[item]

            visited.add(item)
            visited.add(changed_to)
            
            while changed_to in graph:
                changed_to = graph[changed_to]
                visited.add(changed_to)
            answers[item] = changed_to
    return answers

def main():
    q = int(input())
    graph = {}
    for _ in range(q):
        key, val = list(input().split())
        graph[key] = val

    answers = solve(graph)
    print(len(answers), end="\n")

    for key in answers.keys():
        print(f"{key} {answers[key]}", end="\n")

if __name__ == "__main__":
    main()
from collections import defaultdict, Counter

def minimumHammingDistance(source, target, allowedSwaps):
    parent = list(range(len(source)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for a, b in allowedSwaps:
        union(a, b)

    groups = defaultdict(list)
    for i in range(len(source)):
        root = find(i)
        groups[root].append(i)

    result = 0
    for indices in groups.values():
        src_count = Counter()
        
        for i in indices:
            src_count[source[i]] += 1
        
        for i in indices:
            if src_count[target[i]] > 0:
                src_count[target[i]] -= 1
            else:
                result += 1

    return result

source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]

ans = minimumHammingDistance(source, target, allowedSwaps)

print(ans)

source = [1,2,3,4]
target = [1,3,2,4]
allowedSwaps = []

ans = minimumHammingDistance(source, target, allowedSwaps)

print(ans)

source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]

ans = minimumHammingDistance(source, target, allowedSwaps)

print(ans)


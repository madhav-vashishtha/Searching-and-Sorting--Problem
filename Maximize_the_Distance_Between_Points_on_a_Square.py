def maxDistance(side, points, k):
    
    def can_pick(d):
        selected = []
        
        for p in points:
            ok = True
            for q in selected:
                dist = abs(p[0] - q[0]) + abs(p[1] - q[1])
                if dist < d:
                    ok = False
                    break
            if ok:
                selected.append(p)
            if len(selected) >= k:
                return True
        
        return False

    left, right = 0, 2 * side
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        
        if can_pick(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

side = 2
points = [[0,0],[1,2],[2,0],[2,2],[2,1]]
k = 4

print(maxDistance(side, points, k))  

side = 2
points = [[0,2],[2,0],[2,2],[0,0]]
k = 4

print(maxDistance(side, points, k))  

side = 2
points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]]
k = 5

print(maxDistance(side, points, k))  


def minimumOperations(nums):
    c1 = c2 = c3 = 0

    for num in nums:
        if num == 1:
            c1 += 1
        elif num == 2:
            c2 = max(c1, c2) + 1
        else:  
            c3 = max(c1, c2, c3) + 1

    return len(nums) - max(c1, c2, c3)

print(minimumOperations([2,1,3,2,1])) 
print(minimumOperations([1,3,2,1,3,3]))
print(minimumOperations([2,2,2,2,3,3]))


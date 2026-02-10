def findDuplicate(nums):
    low = 1
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        count = 0

        for num in nums:
            if num <= mid:
                count += 1

        if count > mid:
            high = mid  
        else:
            low = mid + 1 

    return low

print(findDuplicate([1,3,4,2,2])) 
print(findDuplicate([3,1,3,4,2])) 
print(findDuplicate([3,3,3,3,3])) 


def majorityElement(nums):
    n = len(nums)
    
    for num in nums:
        count = nums.count(num)
        if count > n // 2:
            return num

print(majorityElement([3, 2, 3]))        
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  



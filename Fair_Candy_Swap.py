def fairCandySwap(aliceSizes, bobSizes):
    sumA = sum(aliceSizes)
    sumB = sum(bobSizes)
    
    diff = (sumB - sumA) // 2  
    
    bob_set = set(bobSizes)   

    for x in aliceSizes:
        if x + diff in bob_set:
            return [x, x + diff]

aliceSizes = [1,1]
bobSizes = [2,2]
print(fairCandySwap(aliceSizes, bobSizes))

aliceSizes = [1,2]
bobSizes = [2,3]
print(fairCandySwap(aliceSizes, bobSizes))

aliceSizes = [2]
bobSizes = [1,3]
print(fairCandySwap(aliceSizes, bobSizes))

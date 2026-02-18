def hightChecker(heights):
    expected = sorted(heights)

    count = 0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1

    return count

heights = [1,1,4,2,1,3]
print(hightChecker(heights))

heights = [5,1,2,3,4]
print(hightChecker(heights))

heights = [1,2,3,4,5]
print(hightChecker(heights))


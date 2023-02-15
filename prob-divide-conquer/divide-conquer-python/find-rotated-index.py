# findRotatedIndex
# Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer. The function should return the index of num in the array. If the value is not found, return -1.

# Constraints:

# Time Complexity: O(log N)

def findRotatedIndex(arr, num):

    '''
        findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12) // -1
        findRotatedIndex([3, 4, 1, 2], 4) // 1
        findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8) // 2
        findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3) // 6
        findRotatedIndex([37, 44, 66, 102, 10, 22], 14) // -1
    '''
    if num in arr:
        return arr.index(num)
    else:
        return -1


print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12))
print(findRotatedIndex([3, 4, 1, 2], 4))
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8))
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3))
print(findRotatedIndex([37, 44, 66, 102, 10, 22], 14))

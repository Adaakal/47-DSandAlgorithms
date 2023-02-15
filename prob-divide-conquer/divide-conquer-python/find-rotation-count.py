# findRotationCount
# Write a function called findRotationCount which accepts an array of distinct numbers sorted in increasing order. The array has been rotated counter-clockwise n number of times. Given such an array, find the value of n.

# Constraints:

# Time Complexity: O(log N)

def findRotationCount(arr):
    '''
    findRotationCount([15, 18, 2, 3, 6, 12]) // 2
    findRotationCount([7, 9, 11, 12, 5]) // 4
    findRotationCount([7, 9, 11, 12, 15]) // 0
    '''
    n = len(arr)
    left, right = 0, n-1
    
    while left < right:
        if arr[left] <= arr[right]:
            return left
        
        mid = (left + right)//2
        prev = (mid - 1)%n
        after = (mid + 1)%n
        
        if arr[mid] <= arr[after] and arr[mid] <= arr[prev]:
            return mid
        
        if arr[mid] <= arr[after]:
            right = mid + 1
        else:
            left = mid + 1
            
    return -1
    

print(findRotationCount([15, 18, 2, 3, 6, 12]))

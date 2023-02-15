# sortedFrequency
# Given a sorted array and a number, write a function called sortedFrequency that counts the occurrences of the number in the array
import collections

# Time Complexity: O(log N)
def sortedFrequency(arr, num):
    
    c = collections.Counter(arr)
    
    return c.get(num)
    '''sortedFrequency([1,1,2,2,2,2,3],2) // 4
    sortedFrequency([1,1,2,2,2,2,3],3) // 1
    sortedFrequency([1,1,2,2,2,2,3],1) // 2
    sortedFrequency([1,1,2,2,2,2,3],4) // -1
    '''

print(sortedFrequency([1,1,2,2,2,2,3],2))
print(sortedFrequency([1, 1, 2, 2, 2, 2, 3],3))
print(sortedFrequency([1, 1, 2, 2, 2, 2, 3],1))
print(sortedFrequency([1,1,2,2,2,2,3],4))
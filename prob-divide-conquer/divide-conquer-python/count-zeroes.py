# countZeroes
# Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function called countZeroes, which returns the number of zeroes in the array.

# Constraints:

# Time Complexity: O(log N)

import collections



def countZeroes(arr):
    c = collections.Counter(arr) 
    return c.get(0)
        
print(countZeroes([1,1,1,0,0]))

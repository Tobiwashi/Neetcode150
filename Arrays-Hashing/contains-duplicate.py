''' Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false


Intuition

Since this problem is asking to remember if a value exists with no other constraints I immediately 
am thinking I should iterate through the numbers array and save any non duplicated values to a set.
If the value exists inside of the set already, return True. If there are none found by the end of the loop
return false.

'''

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        stored_values = {}

        for num in nums:
            if num in stored_values:
                return True
            else:
                stored_values.add(num)
        
        return False
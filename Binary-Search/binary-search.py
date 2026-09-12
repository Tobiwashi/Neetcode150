'''
Binary Search
Easy
Topics
Company Tags
Hints
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1

Intuition 
Since this list is already sorted I can use this to create a simple binary search algorithm that splits the array into halves that eliminate one side per
search resulting in o log n runtime 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        midpoint = len(nums) // 2
        end = len(nums) -1

        while start <= end:
            if target == nums[midpoint]:
                return midpoint
            if target > nums[midpoint]:
                start = midpoint + 1
                midpoint = (end - start) // 2 + start
            if target < nums[midpoint]:
                end = midpoint -1
                midpoint = (end - start) // 2 + start
        
        return -1
'''
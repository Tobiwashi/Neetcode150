'''

PROBLEM 

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

INTUITION 

This problem wants me to compare two things at opposing ends so I will use two pointers and have them iterate over the indexes of the string comparing the values on both sides
returning true after the two pointers converge on each other 

'''

#Solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if left < right and s[left].isalnum() == False:
                while left < right and s[left].isalnum() == False:
                    left += 1 

            if left < right and s[right].isalnum() == False:
                while left < right and s[right].isalnum() == False:
                    right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1

            else:
                return False

        return True
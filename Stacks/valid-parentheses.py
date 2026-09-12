'''

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Intuition 
They want a group of parentheses that need to be solved in reverse order so I just need to keep track of the opening parentheses and make sure that the latest 
closing corresponds with the latest opening using a stack to keep the opening brackets and a hashmap to keep key value pairs of the closing brachets

5

'''
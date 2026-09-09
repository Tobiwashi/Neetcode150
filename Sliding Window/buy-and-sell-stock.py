'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0


Intuition

This problem is asking me to keep track of two different values that moves independently of each from left to right so 
I'm immediately thinking that I'll need to do a sliding window with two pointers. The beginning of the window keeping record of the lowest 
day to buy and the other end of the window sliding outwards to find either a new lowest day or a new highest profit.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_buy = 0
        highest_sell = 1
        profit = 0

        while highest_sell <= len(prices) - 1:
            
            # Determine potential profit
            if (prices[highest_sell] - prices[lowest_buy]) > profit:
                profit = prices[highest_sell] - prices[lowest_buy]

            # Comparison to find lower buying price
            if prices[lowest_buy] > prices[highest_sell]:
                lowest_buy = highest_sell
                highest_sell += 1

            else: highest_sell += 1

        return profit
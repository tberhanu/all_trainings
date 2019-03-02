"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 2**0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2**4 = 16
Example 3:

Input: 218
Output: false
"""
def is_power_of_two(n):
   if n == 0:
      return False
   while n != 1:
      if n % 2 != 0:
         return False
      n = n // 2
   return True



print(is_power_of_two(16))
print(is_power_of_two(218))
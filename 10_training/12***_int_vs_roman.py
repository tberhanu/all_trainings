"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four
is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which is written as IX. There are six instances
where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

def int_to_roman(num):
    """Runtime: 120 ms, faster than 74.25% of Python3 online submissions for Integer to Roman.
"""
    dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
           10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    roman = ""
    for val in dict.keys():
        while val <= num:
            num = num - val
            roman = roman + dict[val]
        if num == 0:
            return roman

# print(int_to_roman(3489))

def roman_to_int(roman):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    num = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and dict[roman[i]] < dict[roman[i + 1]]:
            num = num - dict[roman[i]]
        else:
            num = num + dict[roman[i]]
        i = i + 1
    return num


print(roman_to_int("III"))
print(roman_to_int("IV"))
print(roman_to_int("IX"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))

print(roman_to_int("MMMCDLXXXIX"))

print(roman_to_int("MMMCD"))



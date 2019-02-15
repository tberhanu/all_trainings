def roman_to_int(s):
    sum = 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s) - 1):
        if dict[s[i]] < dict[s[i + 1]]:
            sum = sum - dict[s[i]]
        else:
            sum = sum + dict[s[i]]
    sum = sum + dict[s[-1]]
    return sum

print(roman_to_int("III"))
print(roman_to_int("IV"))
print(roman_to_int("IX"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))

"""
Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

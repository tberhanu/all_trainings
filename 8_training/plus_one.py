"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


"""
def plus_one(digits):
    carry = 0
    for i in range(len(digits) - 1, -1, -1):
        if i == len(digits) - 1:
            sum = carry + digits[i] + 1
        else:
            sum = carry + digits[i]
        carry = sum // 10
        remainder = sum % 10
        digits[i] = remainder
        if carry == 0:
            break

    if carry > 0:
        digits = [carry] + digits

    return digits


print(plus_one([9, 9]))
print(plus_one([1, 2, 3]))

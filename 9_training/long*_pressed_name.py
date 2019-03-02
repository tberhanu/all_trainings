"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c,
the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that
it was your friends name, with some characters (possibly none) being long pressed.


Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.

"""

def is_long_pressed(actual, typed):
    """Runtime: 28 ms, faster than 37.73% of Python online submissions for Long Pressed Name.
"""
    actual = setup(actual)
    typed = setup(typed)
    for a, t in zip(actual, typed):
        if a[0] != t[0] or a[1] > t[1]:
            return False
    return True


def setup(string):
    arr = []
    i = 0
    cntr = 1
    while i < len(string):
        if i + 1 == len(string):
            arr.append((string[i], cntr))
        elif string[i] == string[i+1]:
            cntr = cntr + 1
        else:
            arr.append((string[i], cntr))
            cntr = 1
        i = i + 1
    return arr




print(is_long_pressed("saeed", "ssaeed"))
print(is_long_pressed("saeed", "ssaed"))
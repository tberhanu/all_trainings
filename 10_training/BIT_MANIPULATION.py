
"""
&  ---> AND

|  ---> OR

^  ---> XOR Usually used to switch bits to opposite bits via 1111111 bitmask

~  ---> NOT

<< --> LEFT SHIFT   Usually used for making a bit mask

>> --> RIGHT SHIFT  Usually used for making a bit mask


"""
""" Right and Left Shifts """
# a = 0b001100 # 12
# b = 0b000001 # 1
# print(a)       # --> 12
# print(a << b)  # Multiplying by 2 as we shift LEFT by ONE --> 24
# print(a >> b)  # Dividing by 2 as we shift RIGHT by TWO --> 6

""" OR sth with 11111 is powerful enough to make everything 1111111...
    OR sth with 00000 will RETAIN the original
"""
# a = 0b010 # 2
# print(a | 0b111) # --> 7
# print(a | 0b000) # --> 2

""" AND sth with 0000 is powerful enough to make everything 0000000.....
    AND sth with 1111 will RETAIN the original
"""
# a = 0b010 # 2
# print(a & 0b000) # --> 0
# print(a & 0b111) # --> 2

""" XOR sth with 11111 is a SWITCHER to the opposite bit
    XOR sth with 00000 is a RETAINER
"""
# a = 0b010 # 2
# print(a ^ 0b111) # --> 5
# print(a ^ 0b000) # --> 2

#########

""" How really to write negative binaries ???? """
""" How to change positive binary to negative binary
    --> Flip all bits using XOR 1's 
    --> Then add 1 bit
    --> Then insert 1 bit at the front
"""
print(bin(-3))
print(bin(-3 & 0b111)) # You need to tell Python the total number of digits including the
                        # SIGN BIT at the front
print(bin(-3 & 0b1111))
print(bin(-3 & 0b111111))


def get_bit(num, i):
    """ Given a binary num, and int i, how do you know if the i'th bit is 0 or 1 ?
        1. Get a bit mask of 0's except the i'th bit to be 1 via mask = 1 << i
        2  Then (num & mask),  convert all the bits to 0, except the i'th bit
        3. If (num & mask),  is 0, then the i'th bit is also 0, else the i'th bit is 1
    """
    mask = i << i
    return num & mask == 0

def set_bit(num, i):
    """ Given a binary num, set the i'th bit to 1: SETTING A BIT
        1. Get a bit mast of 0's except the i'th bit to be 1 via mask = 1 << i
        2. Then (num | mask),  will keep all the bits as it is but convert the i'th bit to 1
    """
    mask = i << i
    return num | mask


def clear_bits(num, i):
    """ How about converting the i'th bit to 0: CLEARING A BIT
        1. Convert all the bits to 1's via mask = ~(1 << i), except the i'th and then using AND operator will convert
            it to zero, while retaining the remaining bits
    """
    mask = ~(1 << i)
    return num & mask

def update_bit(num, i, val):
    """ How about we'v a value val, and want to replace it with the i'th bit: UPDATE A BIT
        1. If v is 0, use CLEARING A BIT
        2. If v is 1, use SETTING A BIT
    """
    if val == 1:
        return set_bit(num, i)
    if val == 0:
        return clear_bits(num, i)


def update_bit_two(num, i, val):
    """ Same as the above update_bit """
    mask = ~(1 << i)
    return (num & mask) | (val << i)

def clear_lefts(num, i):
    """ Clear left Bits, NETWORK BITS, including the i'th bit
    00100 - 00001 => 00011
    """

    mask = (1 << i) - 1
    return num & mask

def clear_rights(num, i):
    """ Clear right Bits including the i'th bit
        1. Remember -1 is a sequence of all 1's
        2. We shift by i + 1 to include the i'th bit as it counts startfing from 0, not 1
    """
    mask = (-1 << (i + 1))
    return num & mask


"""
33. Given a string of 1's and 0's concatenated together, what's the minimum FLIP from either
1 to 0 or 0 to 1 so that all zeroes placed to the left and all ones placed to the right.
EX. "11011" --> 1 b/c "11111"
Ex. "10010" --> 2 b/c "00000" or "00011"
"""
def minimun_flip(string):

    arr = []
    for center in range(len(string)):
        lefty = string[:center]
        righty = string[center+1:]
        lefty_ones = lefty.count("1")
        righty_zeroes = righty.count("0")
        arr.append(lefty_ones + righty_zeroes)
    return min(arr)








print(minimun_flip("11011"))
print(minimun_flip("10010"))
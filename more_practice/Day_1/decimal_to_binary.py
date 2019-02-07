"""1. Convert a decimal number to binary
"""


def decimal_to_binary(decimal):
    return bin(decimal)


def convert_decimal_to_binary_manually(num):
    string = ""
    while num != 0:
        string = string + str(num % 2)
        num = num // 2
    return string[::-1]


def binary_to_decimal(binary):
    return int(binary, 2)


def convert_binary_to_decimal_manually(binary):

    return sum(int(b) * (2 ** i) for i, b in enumerate(binary[2:][::-1]))


decimal = 199
binary = decimal_to_binary(decimal)
print(binary)
print(convert_decimal_to_binary_manually(decimal))
print(binary_to_decimal(binary))
print(convert_binary_to_decimal_manually(binary))



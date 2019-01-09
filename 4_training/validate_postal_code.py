#!/usr/bin/env python3

def is_valid_postal_code(code):
    """is_valid_postal_code(code): --> a function validating the integer input by checking the minimum(1000000)
    and maximum(9999999) boundaries, and also by checking that there is no same number placed every other digit.

    --> I followed the rule of NOT USING "IF", but still I would like comments and suggestions if there is a better
    and recommended way to do it.

    :param code: Integer
    :return: Boolean
    """

    code = str(code)
    code1 = code[::2]
    code2 = code[1:][::2]
    # print(code1)
    # print(code2)

    return int(code) >= 1000000 and int(code) <= 9999999 and \
           not(any(c1 == c2 for c1, c2 in zip(code1, code1[1:]))
            or any(c1 == c2 for c1, c2 in zip(code2, code2[1:])) )



if __name__ == "__main__":
    code = 9067830
    print(is_valid_postal_code(code))
    code = 1214267
    print(is_valid_postal_code(code))
    code = 5235639
    print(is_valid_postal_code(code))
    code = 5525236
    print(is_valid_postal_code(code))
    code = 123456
    print(is_valid_postal_code(code))
    code = 1234455
    print(is_valid_postal_code(code))


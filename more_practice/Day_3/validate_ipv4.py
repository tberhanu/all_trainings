""" QUESTION 5"""

def validate_ipv4(string):
    import re
    pattern = re.compile(r'(^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$|^[0-1]{8}\.[0-1]{8}\.[0-1]{8}\.[0-1]{8}$)')
    match = pattern.match(string)
    return bool(match)


string = "255.255.255.0"
print(validate_ipv4(string))
string = "255.255.255.00000000"
print(validate_ipv4(string))
string = "11110000.00110011.00000000.11111111"
print(validate_ipv4(string))

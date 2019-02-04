"""
37. Given txt = "4.5 5.5 -0.7 +7.7 4 5 .9 .99", return all the valid float numbers
"""
def identify_floats(string):
    import re
    pattern = re.compile(r'[+-]?[0-9]*\.[0-9]+')
    matches = pattern.findall(string)
    return matches











text = "4.5 5.5 -0.7 +7.7 4 5 .9 .99"
print(identify_floats(text))
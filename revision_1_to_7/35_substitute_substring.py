"""
35. Given str, substitute " && " by " and ", also " || " by " or "
Solve this problem using i) Regex sub ii) string replace
"""
import re
def substitute(string):
    string = re.sub(r'(?<= )(&&)(?= )', r'and', string)
    string = re.sub(r'(?<= )(\|\|)(?= )', r'or', string)
    return string




string = "here is && and || ofcourse not&& or|| aha"
print(substitute(string))
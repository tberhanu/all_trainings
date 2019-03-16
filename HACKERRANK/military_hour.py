"""https://www.hackerrank.com/challenges/time-conversion/problem"""
""" Time conversion from 12 hour to 24 hour"""
def timeConversion(s):
    status = s[-2:]
    pure = s[:-2]
    hour = s[0:2]
    if hour == "12" and status == "am":
        return "00" + pure[2:]
    h = hour if hour[0] != "0" else hour[1:]
    h = int(h)
    if h >= 1 and status == "pm":
        hour = str(h + 12)
        return hour + pure[2:]
    return pure

print(timeConversion("07:05:45pm"))
print(timeConversion("12:45:54PM"))
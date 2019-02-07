"""
3. Write a program to find difference between two given dates and time
 (format of the input will be like time 1 : dd/mm/yyyy hh:mm:ss. Time 2 : dd/mm/yyyy hh:mm:ss)
"""
from datetime import datetime


def get_interval(d1, d2):
    str1, str2 = d1.split()
    date1, month1, year1 = str1.split("/")
    hour1, min1, sec1 = str2.split(":")
    d1 = datetime(int(year1), int(month1), int(date1), int(hour1), int(min1), int(sec1))

    str1, str2 = d2.split()
    date2, month2, year2 = str1.split("/")
    hour2, min2, sec2 = str2.split(":")
    d2 = datetime(int(year2), int(month2), int(date2), int(hour2), int(min2), int(sec2))

    return d2 - d1



date1 = "11/02/1960 10:10:10"
date2 = "27/08/1988 10:10:10"
print(get_interval(date1, date2))
print("------------------")
d = "30/06/1988 12:12:12"
b = "28/02/1999 09:21:41"
print(get_interval(d, b))


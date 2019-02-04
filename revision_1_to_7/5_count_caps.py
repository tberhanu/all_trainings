"""
5. Given a statement, count the number of capital/small letters
"""

def count_capitals_and_smalls(string):

    caps = sum(1 for s in string if s.isupper())

    return (caps, len(string.replace(" ", "")) - caps)




print(count_capitals_and_smalls("Strings Are Powerful"))
"""
27. Given a str, find all substrings that contains two or more vowels. Also, these substrings
must lie in b/n 2 consonants and should contain vowels only.
Ex. "rabcdeefgyYhFjkIoomnpOeorteeeeet" --> Ioo, Oeo, eeeeee
"""
import re
def filter(string):

    pattern = re.compile(r'(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])', re.I)

    matches = pattern.findall(string)
    return matches









print(filter("rabcdeefgyYhFjkIoomnpOeorteeeeet"))
      # --> Ioo, Oeo, eeeeee

""" This is AMAZING CODE done by Tess, I feel good cracking it"""

"""https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps"""

def sherlock_anagrams(string):
    counter = 0
    start = 0
    while start < len(string): # Let's FIX the START INDEX, start = 0, 1, ...
        end = start + 1  # Then Let's FIX the size of the word by FIXING the END INDEX = 1, 2, ...
        while end <= len(string):
            target = "".join(sorted(string[start:end])) # Let's FIX the TARGET word if [start:end] size
            start2, end2 = start, end # Needed to keep shifting the [start:end] >> [start+i:end+i]
            count = 0
            while end2 <= len(string):
                substring = "".join(sorted(string[start2:end2])) # D/t substrings of the SAME SIZE
                if sorted(substring) == sorted(target): # checking if they're ANAGRAMS
                    count = count + 1
                start2 += 1
                end2 += 1
            counter = counter + (count - 1) # subtracting ONE b/c we include the TARGET itself
                                            # when comparing with others
            # print(count)
            end += 1
        start += 1
    return counter
print(sherlock_anagrams("cdcd"))
print(sherlock_anagrams("abba"))
print(sherlock_anagrams("ifailuhkqq"))
print(sherlock_anagrams("abcd"))

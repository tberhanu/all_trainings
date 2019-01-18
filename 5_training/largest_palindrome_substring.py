# https://www.hackerrank.com/contests/cisco-hackathon/challenges/largest-palindromic-substring
def largest_palindrome_substring(string):
    save = ""

    for i in range(len(string)):

        for j in range(len(string), -1, -1):

            str = string[i:j]
            if str == str[::-1] and len(str) > len(save):
                save = str
                break
        next = string[i+1:]
        if len(save) >= len(next):
            return save


# print(largest_palindrome_substring("hackerrekcahba"))
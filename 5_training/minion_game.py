# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    stuart, kevin = 0, 0
    i = 0
    while i < len(string):
        vowels = "aeiouAEIOU"
        if string[i] in vowels:
            kevin = kevin + len(string[i:])
        else:
            stuart = stuart + len(string[i:])
        i = i + 1
    if stuart == kevin:
        print("Draw")
        return "Draw"
    elif stuart > kevin:
        print("Stuart", stuart)
        return "Stuart {}".format(stuart)
    else:
        print("Kevin", kevin)
        return "Kevin {}".format(kevin)

string = "BANANA"
minion_game(string)
string2 = "BAANANAS"
minion_game(string2)
string = "BANANANAAAS"
minion_game(string)
def crosswordPuzzle(crossword, words):
    k = 0
    for i in range(10):
        for j in range(10):
            s = crossword[i][j]
            if s == "-":
                fill_up(crossword, i, j, words[k])
                k += 1
    return crossword


def fill_up(crossword, i, j, word):
    index = len(word) - 1
    if i + 1 < 10 and crossword[i+1][j] != "+":
        cntr = 0
        while i + 1 < 10 and crossword[i+1][j] != "+":
            cntr = cntr + 1
            i = i + 1

        while cntr >= 0:
            crossword[i + cntr][j] = word[index]
            index -= 1
            cntr -= 1


    index = len(word) - 1
    if j + 1 < 10 and crossword[i][j + 1] != "+":
        cntr = 0
        while j + 1 < 10 and crossword[i][j + 1] != "+":
            cntr = cntr + 1
            j = j + 1

        while cntr >= 0:
            crossword[i][j + cntr] = word[index]
            index -= 1
            cntr -= 1



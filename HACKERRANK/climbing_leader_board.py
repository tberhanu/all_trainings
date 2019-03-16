def foo(board, scores):

    board2 = sorted(list(set(board)), reverse=True)
    scores = zip(scores, range(len(scores)))
    scores2 = sorted(scores, reverse=True)


    ranks = []
    rank = 0
    i, j = 0, 0
    while i < len(board2) and j < len(scores2):

        if scores2[j][0] >= board2[i]:
            ranks.append(rank + 1)
            j += 1
        elif j == len(scores2) -1 and i == len(board2) - 1 and scores2[j][0] < board2[i]:
            ranks.append(rank + 2)
            break

        else:
            i += 1
            rank += 1

    return ranks

print(foo([100, 100, 50, 40, 10], [105, 100, 80, 30, 10, 5]))







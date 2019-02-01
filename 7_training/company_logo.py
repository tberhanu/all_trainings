from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):

    pass


class Main:

    string = "zzzaaabbbb"

    [print(*c) for c in OrderedCounter(sorted(string)).most_common(3)]




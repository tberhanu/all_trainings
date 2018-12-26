def counter(str):
    upper = []
    lower = []
    for s in str:
        if not s.isalpha():
            continue
        elif s == s.lower():
            lower.append(s)
        else:
            upper.append(s)

    print ("UPPER CASE {}".format(len(upper)))
    print ("LOWER CASE {}".format(len(lower)))


counter("Hello world!")

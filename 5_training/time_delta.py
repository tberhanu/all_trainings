
from datetime import datetime as dt

def time_delta(t1, t2):

    fmt = '%a %d %b %Y %H:%M:%S %z'
    print(int(abs((dt.strptime(t1, fmt) -
                   dt.strptime(t2, fmt)).total_seconds())))
    return int(abs((dt.strptime(t1, fmt) -
                   dt.strptime(t2, fmt)).total_seconds()))

t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"
time_delta(t1, t2)
print(time_delta(t1, t2))
t3 = "Sat 02 May 2015 19:54:36 +0530"
t4 = "Fri 01 May 2015 13:54:36 -0000"
print(time_delta(t3, t4))


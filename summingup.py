# ksnt
# sum up the numbers from 0 to 0
# ex)100111101100 => 100123401200

sequence = "100111101100"

import functools

def count(seq):
    result = []
    flag = 0
    for i in map(int,seq):
        if i == 0:
            flag = 0
            result.append(i)
        else:
            flag += 1
            result.append(flag)
    return(map(str,result))


functools.reduce(lambda x,y: x+y, count(sequence))

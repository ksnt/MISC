def main(s):
    """Notice: this is a foolish way to calculate sum of divisors from given natural number
       How to use:
       $ python3 sum_of_divisors.py 10
       >8
    """
    result = []
    for i in range(1,s):
        if(s%i==0):
            result.append(i)
    return(sum(result))

if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) > 1:
        s = args[1]
    print(main(int(s)))

def array_left_rotation(a, n, k):
    if k % n == 0:
        return a
    else:
        l = k % n
        b = a[l:]
        for i in a[:l]:
            b.append(i)
        return b
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

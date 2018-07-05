'''input
5 3
1 2 4 8 16
49

20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999
10988865195

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    from itertools import accumulate
    n, k = list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))
    mod_a = list(accumulate(a))
    total = 0

    for i in range(n - k + 1):
        total += mod_a[i + k] - mod_a[i]

    print(total)

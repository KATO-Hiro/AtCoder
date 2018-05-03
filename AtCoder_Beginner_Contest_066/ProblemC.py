'''input
6
0 6 7 6 7 0
0 6 6 0 7 7

4
1 2 3 4
4 2 1 3

3
1 2 3
3 1 2

1
1000000000
1000000000

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n = int(input())
    a = list(map(str, input().split()))
    odd = a[::2]
    even = a[1::2]

    if n % 2 == 0:
        result = even[::-1] + odd
    else:
        result = odd[::-1] + even

    print(' '.join(result))

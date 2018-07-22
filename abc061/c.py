'''input
10 500001
1 100000
1 100000
1 100000
1 100000
1 100000
100000 100000
100000 100000
100000 100000
100000 100000
100000 100000
100000

10 500000
1 100000
1 100000
1 100000
1 100000
1 100000
100000 100000
100000 100000
100000 100000
100000 100000
100000 100000
1

3 3
1 1
2 2
3 3
2

3 4
1 1
2 2
3 3
3

3 100001
5 1
4 100000
6 99999
5

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n_max = 10 ** 5
    n, k = list(map(int, input().split()))
    a = [0 for _ in range(n_max + 1)]

    # See:
    # https://atcoder.jp/img/abc061/editorial.pdf
    for i in range(n):
        ai, bi = list(map(int, input().split()))
        a[ai] += bi

    for j in range(n_max + 1):
        if a[j] >= k:
            print(j)
            exit()
        else:
            k -= a[j]

'''input
15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5
YES

5
3 1 4 1 5
3
5 4 3
YES

7
100 200 500 700 1200 1600 2000
6
100 200 500 700 1600 1600
NO

1
800
5
100 100 100 100 100
NO

'''

# -*- coding: utf-8 -*-

# CODE FESTIVAL 2017 A
# Problem B

if __name__ == '__main__':
    from collections import Counter

    n = int(input())
    ds = Counter(list(map(int, input().split())))
    m = int(input())
    ts = Counter(list(map(int, input().split())))

    for t_key, t_value in ts.items():
        if (ds[t_key] - t_value) < 0:
            print('NO')
            exit()

    print('YES')

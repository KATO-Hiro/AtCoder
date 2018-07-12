'''input
2 29
NO

1 1
YES

'''

# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    m, d = list(map(int, input().split()))

    if m % d == 0:
        print('YES')
    else:
        print('NO')

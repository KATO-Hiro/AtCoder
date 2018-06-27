# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    d, n = list(map(int, input().split()))

    if n != 100:
        print((100 ** d) * n)
    else:
        print((100 ** d) * (n + 1))

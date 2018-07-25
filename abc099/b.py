# -*- coding: utf-8 -*-
# AtCoder Beginner Contest
# Problem B


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    n = b - a
    print(n * (n - 1) // 2 - a)

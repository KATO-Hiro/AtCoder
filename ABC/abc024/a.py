# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    a, b, c, k = list(map(int, input().split()))
    s, t = list(map(int, input().split()))
    total = a * s + b * t

    if s + t >= k:
        total -= c * (s + t)

    print(total)

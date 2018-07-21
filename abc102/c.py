# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    total = 0

    for i in range(n):
        a[i] -= i + 1

    sorted_a = sorted(a)
    b = sorted_a[n // 2]

    for i in range(n):
        total += abs(a[i] - b)

    print(int(total))

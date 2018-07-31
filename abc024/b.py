# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    n, t = list(map(int, input().split()))
    a = [int(input()) for _ in range(n)]
    duration = t

    for i in range(1, n):
        if a[i - 1] + t > a[i]:
            duration += a[i] - a[i - 1]
        else:
            duration += t

    print(duration)


if __name__ == '__main__':

    main()

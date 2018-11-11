# -*- coding: utf-8 -*-


def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    tmp = [0 for _ in range(n)]
    diff = 10 ** 6

    for i, hi in enumerate(h):
        tmp[i] = abs(a - (t - hi * 0.006))

    ans = 0

    for index, j in enumerate(tmp, 1):
        if j < diff:
            diff = j
            ans = index

    print(ans)


if __name__ == '__main__':
    main()

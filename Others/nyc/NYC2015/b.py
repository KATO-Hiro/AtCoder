# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted([int(input()) for _ in range(n)])
    ans = 1
    weight = a[0]

    for i in range(1, n):
        if a[i] > weight:
            weight += a[i]
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()

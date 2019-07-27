# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if b[i] - a[i] >= 0:
            ans += a[i]
            b[i] -= a[i]
            a[i] = 0

            if b[i] - a[i + 1] >= 0:
                ans += a[i + 1]
                b[i] -= a[i + 1]
                a[i + 1] = 0
            else:
                ans += b[i]
                a[i + 1] -= b[i]
                b[i] = 0
        else:
            ans += b[i]
            a[i] -= b[i]
            b[i] = 0

    print(ans)


if __name__ == '__main__':
    main()

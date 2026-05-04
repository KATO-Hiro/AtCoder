# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(1)
    else:
        for i in range(n - 1):
            a1, a2 = a[i], a[i + 1]

            if a1 == 0 or a2 == 0:
                continue
            if a1 == a2:
                continue
            elif a1 > a2:
                a[i] += a2 // 2
                a[i + 1] = 0
            else:
                a[i + 1] += a1 // 2
                a[i] = 0

        ans = 0

        for ai in a:
            if ai == 0:
                continue

            ans += 1

        print(ans)


if __name__ == "__main__":
    main()

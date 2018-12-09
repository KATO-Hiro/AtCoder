# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)][::-1]
    ans = 0

    for i in range(n):
        p, q = divmod(a[i], 2)
        ans += p

        if q == 1:
            if (i + 1 <= n - 1) and (a[i + 1] >= 1):
                ans += 1
                a[i + 1] -= 1

    print(ans)


if __name__ == '__main__':
    main()

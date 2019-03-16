# -*- coding: utf-8 -*-


def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        a = list(map(int, input().split()))
        total = c

        for j in range(m):
            total += a[j] * b[j]

        if total > 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()

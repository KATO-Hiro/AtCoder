# -*- coding: utf-8 -*-


def main():
    from statistics import median
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]

    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

    a = sorted(a)
    b = sorted(b)
    ans = 1
    m = median(b) - median(a)

    if n % 2 == 0:
        ans += int(2 * m)
    else:
        ans += m

    print(ans)


if __name__ == "__main__":
    main()

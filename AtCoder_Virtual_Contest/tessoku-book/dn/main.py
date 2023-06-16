# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**6 + 10)

    input = sys.stdin.readline

    x, y = map(int, input().split())
    ans = list()

    def gcd(x, y):
        if x == 0 or y == 0:
            return None, None

        if x == 1 and y == 1:
            return None, None

        ans.append((x, y))

        if x >= y:
            p, q = divmod(x, y)

            for i in range(p - 1, 0, -1):
                ans.append((i * y + q, y))

            gcd(x % y, y)
        else:
            p, q = divmod(y, x)

            for i in range(p - 1, 0, -1):
                ans.append((x, i * x + q))

            gcd(x, y % x)

    gcd(x, y)

    size = len(ans)

    if (1, 1) in ans:
        size -= 1

    print(size)

    if size > 0:
        for xi, yi in ans[::-1]:
            if xi > 1 or yi > 1:
                print(xi, yi)


if __name__ == "__main__":
    main()

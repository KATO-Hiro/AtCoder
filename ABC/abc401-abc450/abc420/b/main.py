# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    count = [0] * n

    for j in range(m):
        x, y = 0, 0

        for i in range(n):
            if s[i][j] == "0":
                x += 1
            else:
                y += 1

        if x == 0 or y == 0:
            for i in range(n):
                count[i] += 1
        elif x < y:
            for i in range(n):
                if s[i][j] == "0":
                    count[i] += 1
        elif x > y:
            for i in range(n):
                if s[i][j] == "1":
                    count[i] += 1

    d = defaultdict(list)

    for i, ci in enumerate(count, 1):
        d[ci].append(i)

    d_max = max(d.keys())

    print(*sorted(d[d_max]))


if __name__ == "__main__":
    main()

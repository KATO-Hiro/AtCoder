# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(n)]
    d = defaultdict(int)

    for i in range(n):
        if i + m > n:
            break

        for j in range(n):
            if j + m > n:
                break

            pattern = list()

            for x in range(m):
                for y in range(m):
                    pattern.append(s[i + x][j + y])

            d["".join(pattern)] += 1

    print(len(d.keys()))


if __name__ == "__main__":
    main()

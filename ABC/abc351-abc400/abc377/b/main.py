# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h = w = 8
    s = [list(input().rstrip()) for _ in range(h)]
    rows, cols = set(), set()

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                rows.add(i)
                cols.add(j)

    ans = 0

    for i in range(h):
        for j in range(w):
            if i in rows or j in cols:
                continue

            ans += 1
    print(ans)


if __name__ == "__main__":
    main()

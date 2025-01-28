# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    inf = 10**5
    h_min, h_max = inf, -inf
    w_min, w_max = inf, -inf

    for i in range(h):
        for j in range(w):
            if s[i][j] != "#":
                continue

            h_min = min(h_min, i)
            h_max = max(h_max, i)

            w_min = min(w_min, j)
            w_max = max(w_max, j)

    ans = "Yes"

    for i in range(h_min, h_max + 1):
        for j in range(w_min, w_max + 1):
            if s[i][j] == ".":
                ans = "No"
                break

    print(ans)


if __name__ == "__main__":
    main()

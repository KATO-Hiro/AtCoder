# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b, c, d = map(int, input().split())
    ans = [["."] * (d - c + 1) for _ in range(b - a + 1)]
    b -= a
    d -= c
    r = set()
    s = set()

    for _ in range(n):
        pi, qi = map(int, input().split())
        pi -= a
        qi -= c
        ri, si = pi + qi, pi - qi
        r.add(ri)
        s.add(si)

    for i in range(b + 1):
        for j in range(d + 1):
            if (i + j) in r or (i - j) in s:
                ans[i][j] = "#"

    for ans_i in ans:
        print("".join(map(str, ans_i)))


if __name__ == "__main__":
    main()

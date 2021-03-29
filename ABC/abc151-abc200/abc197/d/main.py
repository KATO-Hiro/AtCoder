# -*- coding: utf-8 -*-


def main():
    from math import pi
    from cmath import rect
    import sys

    input = sys.stdin.readline

    n = int(input())
    x0, y0 = map(int, input().split())
    xn2, yn2 = map(int, input().split())

    p0 = complex(x0, y0)
    pn2 = complex(xn2, yn2)
    o = (p0 + pn2) / 2
    r = rect(1, 2 * pi / n)
    ans = o + r * (p0 - o)

    print(ans.real, ans.imag)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    def f(p, q, r):
        return q - p == r - q

    ans = 0

    for x in range(-300, 300):
        ok = False

        if f(a, b, x):
            ok = True
        if f(a, x, b):
            ok = True
        if f(b, a, x):
            ok = True
        if f(b, x, a):
            ok = True
        if f(x, a, b):
            ok = True
        if f(x, b, a):
            ok = True

        if ok:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

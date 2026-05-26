# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r, m = map(int, input().split())
    s1 = set()
    s2 = set()

    for i in range(n):
        pi, ki = map(int, input().split())

        if l <= pi <= r:
            s1.add(i)
        if ki <= m:
            s2.add(i)

    ans = len(s1 & s2)
    print(ans)


if __name__ == "__main__":
    main()

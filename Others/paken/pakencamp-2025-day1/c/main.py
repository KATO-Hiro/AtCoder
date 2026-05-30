# -*- coding: utf-8 -*-


def solve():
    n, m = map(int, input().split())
    a = sorted(set(map(int, input().split())), reverse=True)
    b = sorted(set(map(int, input().split())), reverse=True)
    n = min(n, 2)
    m = min(m, 2)
    a2 = a[:n] + a[-n:]
    b2 = b[:m] + b[-m:]
    c = set()

    for a2i in a2:
        for b2j in b2:
            c.add(a2i * b2j)

    c = sorted(c, reverse=True)

    if len(c) <= 1:
        print("None")
    else:
        print(c[1])


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

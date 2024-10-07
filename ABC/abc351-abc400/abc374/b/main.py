# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    n, m = len(s), len(t)

    if n > m:
        t += "?" * (n - m)
    elif m > n:
        s += "?" * (m - n)

    ans = 0

    for i, (si, ti) in enumerate(zip(s, t), 1):
        if si != ti:
            ans = i
            break

    print(ans)


if __name__ == "__main__":
    main()

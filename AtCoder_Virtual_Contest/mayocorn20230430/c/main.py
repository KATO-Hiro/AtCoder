# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = input().rstrip()
    t = [0] * (n + 1)
    prev = ""

    for i, si in enumerate(s, 1):
        t[i] = t[i - 1]

        if prev == "A" and si == "C":
            t[i] += 1

        prev = si
    
    for _ in range(q):
        li, ri = map(int, input().split())
        print(t[ri] - t[li])


if __name__ == "__main__":
    main()

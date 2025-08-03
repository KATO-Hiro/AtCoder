# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    x, y = [], []  # i + Ai, j - Aj

    for i, ai in enumerate(a):
        x.append(i + ai)
        y.append(i - ai)

    y = y[::-1]
    count = Counter(y)
    ans = 0

    for xi in x[:-1]:
        prev = y[-1]
        y.pop()
        count[prev] -= 1

        ans += count[xi]

    print(ans)


if __name__ == "__main__":
    main()

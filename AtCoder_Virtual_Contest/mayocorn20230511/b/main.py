# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from string import ascii_lowercase

    input = sys.stdin.readline

    x = input().rstrip()
    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    alpha = ascii_lowercase
    d = defaultdict(str)

    for ai, xi in zip(alpha, x):
        d[xi] = ai

    ans = list()

    for si in s:
        ti = ""

        for sij in si:
            ti += d[sij]

        ans.append((ti, si))

    for _, si in sorted(ans):
        print(si)


if __name__ == "__main__":
    main()

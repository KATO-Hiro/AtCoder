# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    d = defaultdict(int)

    for i in range(n):
        for j in range(i + 1, n):
            t = list(s[:])
            t[i], t[j] = t[j], t[i]
            d["".join(t)] += 1

    print(len(d.keys()))


if __name__ == "__main__":
    main()

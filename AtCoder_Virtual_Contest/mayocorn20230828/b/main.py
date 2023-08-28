# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()
    c = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ci in enumerate(c):
        d[ci].append(i)

    ans = [""] * n

    for values in d.values():
        size = len(values)

        for i in range(size):
            ni = (i - 1 + size) % size
            ans[values[i]] = s[values[ni]]

    print("".join(ans))


if __name__ == "__main__":
    main()

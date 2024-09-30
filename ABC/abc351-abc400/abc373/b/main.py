# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import pairwise
    from string import ascii_uppercase

    input = sys.stdin.readline

    s = input().rstrip()
    d = defaultdict(int)

    for i, si in enumerate(s):
        d[si] = i

    ans = 0

    for first, second in pairwise(ascii_uppercase):
        ans += abs(d[second] - d[first])

    print(ans)


if __name__ == "__main__":
    main()

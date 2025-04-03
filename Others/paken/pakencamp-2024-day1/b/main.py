# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter
    from math import ceil

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    c = Counter(s)
    d = {"P": 2, "A": 2, "K": 1, "E": 1, "N": 1, "C": 1, "M": 1}
    ans = 0

    for key, count in c.items():
        if key not in d:
            print(-1)
            exit()

        ans = max(ans, ceil(count / d[key]))

    print(ans)


if __name__ == "__main__":
    main()

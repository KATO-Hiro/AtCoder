# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)

    for _ in range(n):
        si = input().rstrip().lower()
        d[si] += 1

    ans = max(d.values())
    print(ans)


if __name__ == "__main__":
    main()

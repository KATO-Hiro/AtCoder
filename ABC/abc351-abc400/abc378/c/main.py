# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(lambda: -1)
    ans = list()

    for i, ai in enumerate(a, 1):
        ans.append(d[ai])
        d[ai] = i

    print(*ans)


if __name__ == "__main__":
    main()

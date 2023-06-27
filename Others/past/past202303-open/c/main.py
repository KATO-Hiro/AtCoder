# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    d = defaultdict(int)

    for i, pi in enumerate(p, 1):
        d[pi] = i

    ans = list()

    for i in range(1, n + 1):
        ans.append(d[i])

    print(*ans)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    ans = list()

    for i, ai in enumerate(a, 1):
        d[ai] += 1

        if d[ai] == 2:
            ans.append(ai)

    print(*ans)


if __name__ == "__main__":
    main()

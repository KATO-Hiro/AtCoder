# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for i, ai in enumerate(a, 1):
        d[ai] = i

    key = -1
    ans = list()

    while True:
        value = d[key]

        if value == 0:
            break

        ans.append(value)
        key = value

    print(*ans)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list()

    for i in range(1, n + 1):
        _ = int(input())
        ai = list(map(int, input().split()))
        a.append(ai)

    x = int(input())
    d = defaultdict(list)

    for i, ai in enumerate(a, 1):
        if x in ai:
            d[len(ai)].append(i)

    size = len(d.keys())
    # print(d)

    if size == 0:
        print(0)
    else:
        key_min = min(d.keys())
        # print(d[key_min])
        print(len(d[key_min]))
        print(*sorted(d[key_min]))


if __name__ == "__main__":
    main()

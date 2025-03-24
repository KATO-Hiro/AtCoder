# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ai in enumerate(a, 1):
        d[ai].append(i)

    candidates = list()

    for key, value in d.items():
        if len(value) >= 2:
            continue

        candidates.append(key)

    if len(candidates) == 0:
        print(-1)
    else:
        number_max = max(candidates)
        print(*d[number_max])


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(list)

    for _ in range(n):
        ci, li = map(int, input().split())
        d[ci].append(li)

    total = 0

    for values in d.values():
        m = len(values)

        for i in range(m):
            for j in range(i + 1, m):
                total += abs(values[i] - values[j])

    print(total)


if __name__ == "__main__":
    main()

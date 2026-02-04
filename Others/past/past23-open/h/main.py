# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ai in enumerate(a):
        d[ai].append(i)

    x, y = 0, 0

    for key, values in d.items():
        size = len(values)

        for i in range(size):
            x += (2 * i - size + 1) * values[i]

        x -= size * (size - 1) // 2
        y += size * (size - 1) * (size - 2) // 6

    ans = x - y
    print(ans)


if __name__ == "__main__":
    main()

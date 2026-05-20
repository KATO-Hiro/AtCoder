# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, k = map(int, input().split())
    f, b = [], []

    for _ in range(n):
        fi, bi = map(int, input().split())
        f.append(fi)
        b.append(bi)

    patterns = product([0, 1], repeat=n)
    ans = 0

    for pattern in patterns:
        summed = 0
        count = 0

        for i, pi in enumerate(pattern):
            if pi == 0:
                summed += b[i]
                count += 1
            else:
                summed += f[i]

        if count == k:
            ans = max(ans, summed)

    print(ans)


if __name__ == "__main__":
    main()

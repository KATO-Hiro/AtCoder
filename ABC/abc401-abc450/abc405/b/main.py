# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for ai in a:
        d[ai] += 1

    for i in range(1, m + 1):
        if d[i] == 0:
            print(0)
            exit()

    for i, ai in enumerate(a[::-1], 1):
        d[ai] -= 1

        for j in range(1, m + 1):
            if d[j] == 0:
                print(i)
                exit()


if __name__ == "__main__":
    main()

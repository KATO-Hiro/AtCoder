# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    d = list(map(int, input().split()))
    d2 = defaultdict(int)

    for _ in range(m):
        pi, si = map(int, input().split())
        d2[pi] = si

    remain = k

    for i, di in enumerate(d, 1):
        if remain <= 0:
            print("No")
            exit()

        remain -= di

        if i not in d2.keys():
            continue

        remain = max(remain, d2[i])

    print("Yes")


if __name__ == "__main__":
    main()

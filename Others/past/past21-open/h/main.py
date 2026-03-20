# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, l, m = map(int, input().split())
    d = list(map(int, input().split()))
    used = []

    for i, di in enumerate(d):
        size = len(used)
        diff = size - m

        if diff < 0 or di - used[diff] >= l:
            used.append(di)

    ans = k - len(used)
    print(ans)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ans = 0

    for i in range(1, n + 1):
        summed = [int(si) for si in list(str(i))]

        if sum(summed) == k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

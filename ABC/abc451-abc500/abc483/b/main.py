# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    k = list(map(int, input().split()))
    ans = [i for i in range(1, n + 1)]

    for ki in k:
        ans = ans[:ki][::-1] + ans[ki:]

        for i in range(ki):
            ans[i] *= -1

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()

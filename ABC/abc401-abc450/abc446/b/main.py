# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    used = [False] * (m + 1)
    used[0] = True

    for _ in range(n):
        __ = int(input())

        x = list(map(int, input().split()))
        ans = 0

        for xi in x:
            if used[xi]:
                continue

            ans = xi
            used[xi] = True
            break

        print(ans)


if __name__ == "__main__":
    main()

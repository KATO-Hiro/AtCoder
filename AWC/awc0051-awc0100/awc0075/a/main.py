# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    r = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if i + 2 >= n:
            break

        if (r[i] < r[i + 1] and r[i + 1] > r[i + 2]) or (
            r[i] > r[i + 1] and r[i + 1] < r[i + 2]
        ):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

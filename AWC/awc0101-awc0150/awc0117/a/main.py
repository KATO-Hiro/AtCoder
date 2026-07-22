# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    inf = 10**18
    ans = -inf

    for i in range(1, n + 1):
        candidate = a[i - 1] + a[i] + a[i + 1]
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    mod = 10**9 + 7
    ans = 1

    # 素因数分解ができる
    for i in range(n):
        ans *= sum(a[i])
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()

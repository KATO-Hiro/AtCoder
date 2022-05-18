# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0

    for i, ai in enumerate(a):
        ans += ai * pow(2, i, mod)
        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()

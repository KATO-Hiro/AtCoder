# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10 ** 9 + 7
    ans = 1

    for i in range(1, n + 1):
        ans *= i
        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()

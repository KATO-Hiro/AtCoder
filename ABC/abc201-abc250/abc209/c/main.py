# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = sorted(list(map(int, input().split())))
    ans = 1
    mod = 10 ** 9 + 7

    for index, ci in enumerate(c):
        ans *= max(0, ci - index)
        ans %= mod
    
    print(ans)


if __name__ == "__main__":
    main()

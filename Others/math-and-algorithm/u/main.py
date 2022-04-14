# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, r = map(int, input().split())
    m = n + 1
    ans = 1

    for i in range(1, r + 1):
        ans *= m - i
        ans //= i
    
    print(ans)


if __name__ == "__main__":
    main()

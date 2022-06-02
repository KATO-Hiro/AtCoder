# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())    
    mod = 2019
    r = min(r, l + mod)
    ans = mod

    for i in range(l, r):
        for j in range(i + 1, r + 1):
            candidate = (i * j) % mod
            ans = min(ans, candidate)
    
    print(ans)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    r = [["-"] * n for _ in range(n)]

    for i in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        r[ai][bi] = "o"
        r[bi][ai] = "x"
    
    for ri in r:
        print(*ri)


if __name__ == "__main__":
    main()

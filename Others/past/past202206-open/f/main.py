# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(h)]
    n = int(input())

    for i in range(n):
        ri, ci = map(int, input().split())
        ri -= 1
        ci -= 1
        s[ri][ci] = 0

        while ri > 0 and s[ri][ci] == 0:
            s[ri][ci], s[ri - 1][ci] = s[ri - 1][ci], s[ri][ci]
            ri -= 1
    
    for si in s:
        print(*si)


if __name__ == "__main__":
    main()

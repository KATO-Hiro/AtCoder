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

        if s[ri][ci] == 0:
            continue

        for j in range(ri, 0, -1):
            s[j][ci] = s[j - 1][ci]
        
        s[0][ci] = 0
    
    for si in s:
        print(*si)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]

    for i in range(h):
        for j in range(w - 1):
            if s[i][j] == "T" and s[i][j + 1] == "T":
                s[i][j] = "P"
                s[i][j + 1] = "C"
    
    for si in s:
        print(*si, sep="")
    

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = list()

    for j in range(w):
        c = list()

        for i in range(h):
            c.append(a[i][j])
        
        b.append(c)
    
    for bi in b:
        print(*bi)


if __name__ == "__main__":
    main()

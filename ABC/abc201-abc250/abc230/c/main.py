# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    h = q - p + 1
    w = s - r + 1
    ans = [['.'] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            x = p + i
            y = r + j
            
            if x + y == a + b or x - y == a - b: 
                ans[i][j] = "#"

    for a in ans:
        print("".join(a))


if __name__ == "__main__":
    main()

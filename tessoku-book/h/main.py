# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(h)]
    q = int(input())
    s = [[0] * (w + 1)]

    for xi in x:
        yi = [0] + list(accumulate(xi))
        s.append(yi)
    
    for i in range(1, h + 1):
        for j in range(w + 1):
            s[i][j] += s[i - 1][j]
            
    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())

        summed = s[ci][di]
        summed -= s[ai - 1][di]
        summed -= s[ci][bi - 1]
        summed += s[ai - 1][bi - 1]

        print(summed)

   

if __name__ == "__main__":
    main()

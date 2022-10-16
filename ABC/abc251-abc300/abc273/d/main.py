# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    h, w, y, x = map(int, input().split())
    n = int(input())
    # グリッドの端部のマスを用意
    rows = defaultdict(lambda: [0, w + 1])
    cols = defaultdict(lambda: [0, h + 1])

    # 壁の位置を行と列でそれぞれ管理
    for i in range(n):
        ri, ci = map(int, input().split())
        rows[ri].append(ci)
        cols[ci].append(ri)
    
    for key, value in rows.items():
        rows[key] = sorted(value)

    for key, value in cols.items():
        cols[key] = sorted(value)

    q = int(input())
    ans = [(0, 0)] * q

    for i in range(q):
        di, li = input().rstrip().split()
        li = int(li)

        if di == "L":
            index = bisect_left(rows[y], x)
            x = max(x - li, rows[y][index - 1] + 1)
        elif di == "R":
            index = bisect_left(rows[y], x)
            x = min(x + li, rows[y][index] - 1)
        elif di == "U":
            index = bisect_left(cols[x], y)
            y = max(y - li, cols[x][index - 1] + 1)
        elif di == "D":
            index = bisect_left(cols[x], y)
            y = min(y + li, cols[x][index] - 1)
        
        ans[i] = (y, x)

    for ri, ci in ans:
        print(ri, ci)


if __name__ == "__main__":
    main()

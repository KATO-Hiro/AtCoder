# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    d = defaultdict(int)

    for xi, yi in xy:
        d[(xi, yi)] += 1
    
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]

            if d[(x2, y1)] >= 1 and d[(x1, y2)] >= 1:
                if len(set(((x1, y1), (x2, y2), (x2, y1), (x1, y2)))) == 4:
                    ans += 1

    print(ans // 2)


if __name__ == "__main__":
    main()

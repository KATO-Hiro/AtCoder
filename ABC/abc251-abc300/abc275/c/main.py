# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    s = [input().rstrip() for _ in range(9)]
    xy = list()
    count = 0

    for x in range(9):
        for y in range(9):
            if s[y][x] == "#":
                xy.append((count, x, y))
                count += 1
            
    ans = 0
    
    for a, b, c, d in combinations(range(count), 4):
        dist = set()

        for e, f in combinations([a, b, c, d], 2):
            _, ex, ey =  xy[e]
            _, fx, fy =  xy[f]
            d = (ex - fx) ** 2 + (ey - fy) ** 2

            dist.add(d)
    
        if len(dist) == 2:
            ans += 1

    # print(s)
    # print(xy)
    print(ans)
    

if __name__ == "__main__":
    main()

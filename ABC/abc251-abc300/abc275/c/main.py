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
                xy.append((x, y))
                count += 1
            
    ans = 0
    
    # points: [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    def is_square(points):
        # See:
        # https://sugim48.hatenadiary.org/entry/20141007/1412679470

        dist = list() 

        for i in range(4):
            x1, y1 = points[i]

            for j in range(i + 1, 4):
                x2, y2 = points[j]

                dx = (x2 - x1) ** 2
                dy = (y2 - y1) ** 2

                dist.append(dx + dy)

        dist = sorted(dist)
        base = dist[0]

        if base == 0:
            return False # duplicated
        
        if dist.count(base) == 4 and dist.count(base * 2) == 2:
            return True
        else:
            return False

    for a, b, c, d in combinations(range(count), 4):
        if is_square((xy[a], xy[b], xy[c], xy[d])):
            ans += 1

    print(ans)
    

if __name__ == "__main__":
    main()

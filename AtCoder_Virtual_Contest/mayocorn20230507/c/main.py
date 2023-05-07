# -*- coding: utf-8 -*-


def main():
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    n = h + w - 2
    ans = 0

    for pattern in combinations(range(n), h - 1):
        pattern = set(pattern)
        i, j = 0, 0
        values = list()
        values.append(a[i][j])

        for x in range(n):
            if x in pattern:
                i += 1
            else:
                j += 1
            
            values.append(a[i][j])
        
        if len(values) == len(set(values)):
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
